#!/usr/bin/env python3
"""Genera o comprueba las copias personales de las tres skills de edición."""

import argparse
import os
import re
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SOURCES = REPO / '.agents' / 'skills'
NAMES = (
    'al-destino-edicion',
    'al-destino-edicion-horizontal',
    'al-destino-edicion-vertical',
)


def package_files(root):
    return {
        p.relative_to(root): p
        for p in root.rglob('*')
        if p.is_file() and '__pycache__' not in p.parts and p.suffix != '.pyc'
    }


def installed_bytes(source):
    if source.suffix != '.md':
        return source.read_bytes()
    content = source.read_text(encoding='utf-8-sig')

    def rebase(match):
        raw = match.group(1).strip('<>')
        if raw.startswith('#') or re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', raw):
            return match.group(0)
        path, separator, anchor = raw.partition('#')
        target = (source.parent / path).resolve()
        # Las dependencias entre estas skills conservan enlaces relativos.
        if target.is_relative_to(SOURCES) or not target.is_relative_to(REPO):
            return match.group(0)
        suffix = separator + anchor if separator else ''
        return f'](<{target.as_posix()}{suffix}>)'

    content = re.sub(r'\]\(([^)]+)\)', rebase, content)
    if source.name == 'SKILL.md':
        parts = content.split('---', 2)
        if len(parts) != 3 or parts[0]:
            raise ValueError(f'Frontmatter no reconocido: {source}')
        note = (
            '\n\n<!-- Generado por scripts/sincronizar-skills-edicion.py; '
            'editar la fuente. -->\n'
            f'Fuente mantenida: [skill del repositorio](<{source.as_posix()}>). '
            f'Trabajar desde la raíz `{REPO.as_posix()}`; '
            'las rutas de trabajo se resuelven allí.\n'
        )
        content = '---' + parts[1] + '---' + note + parts[2]
    return content.encode('utf-8')


def sync(destination, write=False):
    destination = destination.resolve()
    if destination == SOURCES or destination.is_relative_to(SOURCES):
        raise ValueError('El destino debe estar fuera de las fuentes de skills.')
    changes = []
    extras = []
    for name in NAMES:
        source_root = SOURCES / name
        target_root = destination / name
        if not (source_root / 'SKILL.md').is_file():
            raise ValueError(f'Falta la fuente: {source_root}')
        sources = package_files(source_root)
        for relative, source in sources.items():
            target = target_root / relative
            expected = installed_bytes(source)
            if not target.is_file() or target.read_bytes() != expected:
                changes.append((target, expected))
        extras.extend(target_root / p for p in package_files(target_root).keys() - sources.keys())

    # No borrar archivos obsoletos ni sobrescribir un paquete con contenido ajeno.
    if extras:
        for path in sorted(extras):
            print(f'Archivo sin fuente; revisar y archivar manualmente: {path}')
        return 1
    for target, expected in changes:
        if write:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(expected)
        print(f'{"Actualizado" if write else "Diferencia"}: {target}')
    print(f'{len(NAMES)} skills; {len(changes)} archivos {"actualizados" if write else "con diferencias"}.')
    return 0 if write or not changes else 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    codex_root = Path(os.environ.get('CODEX_HOME') or Path.home() / '.codex')
    parser.add_argument('--dest', type=Path, default=codex_root / 'skills',
                        help='Directorio de skills personales; por defecto CODEX_HOME/skills o ~/.codex/skills.')
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument('--check', action='store_true', help='Comprobar sin escribir.')
    modes.add_argument('--write', action='store_true', help='Generar las copias personales.')
    args = parser.parse_args()
    try:
        return sync(args.dest, args.write)
    except (OSError, ValueError) as exc:
        parser.exit(1, f'Error: {exc}\n')


if __name__ == '__main__':
    raise SystemExit(main())
