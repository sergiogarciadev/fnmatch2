# -*- coding: utf-8 -*-

from fnmatch2 import fnmatch2


class TestFilenameMatch(object):
    def test_filename_patterns(self):
        assert(fnmatch2('site.yml', 'site.yml'))
        assert(fnmatch2('site.yml', '**/site.yml'))

        assert(fnmatch2('images/logo.png', '**/*.png'))
        assert(fnmatch2('images/logo.png', 'images/**/*.png'))
        assert(fnmatch2('images/logo.png', '**/images/**/*.png'))
        assert(fnmatch2('images/logo.png', '**/images/**/*.???'))
        assert(fnmatch2('images/logo.png', '**/image?/**/*.???'))

        assert(fnmatch2('images/.gitkeep', '**/.*'))
        assert(fnmatch2('output/.gitkeep', '**/.*'))

        assert(fnmatch2('images/.gitkeep', '**\\.*'))
        assert(fnmatch2('output/.gitkeep', '**\\.*'))

        assert(fnmatch2('.hidden', '**/.*'))
        assert(fnmatch2('sub/.hidden', '**/.*'))
        assert(fnmatch2('sub/sub/.hidden', '**/.*'))
