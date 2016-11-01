# -*- coding: utf-8 -*-

from fnmatch2 import fnmatch2
from fnmatch2 import fnmatchcase2


class TestFilenameMatch(object):
    def test_fnmatch2_patterns(self):
        assert(fnmatch2('site.yml', 'site.yml'))
        assert(fnmatch2('site.yml', '**/site.yml'))

        assert(fnmatch2('SITE.YML', 'site.yml'))
        assert(fnmatch2('SITE.YML', '**/site.yml'))

        assert(fnmatch2('images/logo.png', '*/*.png'))
        assert(not fnmatch2('images/images/logo.png', '*/*.png'))
        assert(not fnmatch2('images/logo.png', '*/*/*.png'))
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

        assert(not fnmatch2('.hidden', '**/hidden'))
        assert(not fnmatch2('sub/.hidden', '**/hidden'))
        assert(not fnmatch2('sub/sub/.hidden', '**/hidden'))

    def test_fnmatchcase2_patterns(self):
        assert(fnmatchcase2('site.yml', 'site.yml'))
        assert(fnmatchcase2('site.yml', '**/site.yml'))

        assert(not fnmatchcase2('SITE.YML', 'site.yml'))
        assert(not fnmatchcase2('SITE.YML', '**/site.yml'))

        assert(fnmatchcase2('images/logo.png', '*/*.png'))
        assert(not fnmatchcase2('images/images/logo.png', '*/*.png'))
        assert(not fnmatchcase2('images/logo.png', '*/*/*.png'))
        assert(fnmatchcase2('images/logo.png', '**/*.png'))
        assert(fnmatchcase2('images/logo.png', 'images/**/*.png'))
        assert(fnmatchcase2('images/logo.png', '**/images/**/*.png'))
        assert(fnmatchcase2('images/logo.png', '**/images/**/*.???'))
        assert(fnmatchcase2('images/logo.png', '**/image?/**/*.???'))

        assert(fnmatchcase2('images/.gitkeep', '**/.*'))
        assert(fnmatchcase2('output/.gitkeep', '**/.*'))

        assert(fnmatchcase2('images/.gitkeep', '**\\.*'))
        assert(fnmatchcase2('output/.gitkeep', '**\\.*'))

        assert(fnmatchcase2('.hidden', '**/.*'))
        assert(fnmatchcase2('sub/.hidden', '**/.*'))
        assert(fnmatchcase2('sub/sub/.hidden', '**/.*'))

        assert(not fnmatchcase2('.hidden', '**/hidden'))
        assert(not fnmatchcase2('sub/.hidden', '**/hidden'))
        assert(not fnmatchcase2('sub/sub/.hidden', '**/hidden'))
