# fnmatch2

[![Build Status](https://travis-ci.org/LawfulHacker/fnmatch2.svg?branch=master)](https://travis-ci.org/LawfulHacker/fnmatch2)
[![Coverage Status](https://coveralls.io/repos/github/LawfulHacker/fnmatch2/badge.svg?branch=master)](https://coveralls.io/github/LawfulHacker/fnmatch2?branch=master)

An improved Unix filename pattern matching.

This library has created to include the Apache Ant wildcard support ('**') to Python fnmatch function.

## Getting Started

Install the package:

    $ pip install fnmatch2

Simple import and use on your code:

    >>> from fnmatch2 import fnmatch2
    >>> fnmatch2('images/logo.png', '**/*.png')
    True

