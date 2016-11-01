# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from setuptools.command.test import test as test_command
from fnmatch2 import __version__


class PyTest(test_command):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        test_command.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        test_command.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import sys
        import pytest

        errno = pytest.main(self.pytest_args)

        sys.exit(errno)


setup(
    name='fnmatch2',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    include_package_data=True,
    package_data={},
    version=__version__,
    description='An improved Unix filename pattern matching',
    long_description='An improved Unix filename pattern matching',
    author='Sergio Garcia',
    author_email='lawfulhacker@gmail.com',
    url='https://github.com/LawfulHacker/fnmatch2',
    download_url='https://github.com/LawfulHacker/fnmatch2/releases',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='fnmatch pattern path',
    entry_points={},
    install_requires=[],
    extras_require={
        'dev': [
            'coveralls>=1.1',
            'pytest>=3.0.3'
        ]
    },
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
)
