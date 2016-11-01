# -*- coding: utf-8 -*-

from fnmatch import fnmatch
from fnmatch import fnmatchcase


def _fnmatch2(fnmatch, filename, pattern):
    pattern = pattern.replace('\\', '/')
    filename = filename.replace('\\', '/')

    filename_parts = filename.split('/')
    pattern_parts = pattern.split('/')

    include_dirs_and_subdirs = False

    for pattern_part in pattern_parts:
        if pattern_part == '**':
            include_dirs_and_subdirs = True
            continue

        pattern_match = False

        while len(filename_parts) > 0:
            filename_part = filename_parts[0]
            filename_parts = filename_parts[1:]

            if fnmatch(filename_part, pattern_part):
                pattern_match = True
                include_dirs_and_subdirs = False
                break

            if include_dirs_and_subdirs:
                continue

            return False

        if not pattern_match:
            return False

    return True


def fnmatch2(filename, pattern):
    return _fnmatch2(fnmatch, filename, pattern)


def fnmatchcase2(filename, pattern):
    return _fnmatch2(fnmatchcase, filename, pattern)
