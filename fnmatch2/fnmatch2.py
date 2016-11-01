# -*- coding: utf-8 -*-

from fnmatch import fnmatch


def fnmatch2(path, pattern):
    pattern = pattern.replace('\\', '/')
    path = path.replace('\\', '/')

    parts = path.split('/')
    pattern_parts = pattern.split('/')

    include_dirs_and_subdirs = False

    for pattern_part in pattern_parts:
        if pattern_part == '**':
            include_dirs_and_subdirs = True
            continue

        while len(parts) > 0:
            part = parts[0]
            parts = parts[1:]

            if fnmatch(part, pattern_part):
                include_dirs_and_subdirs = False
                break

            if include_dirs_and_subdirs:
                continue

            return False
    return True
