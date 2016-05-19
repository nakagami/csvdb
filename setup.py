import sys
from distutils.core import setup, Command


class TestCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        from csvdb import test_csvdb
        import unittest
        unittest.main(test_csvdb, argv=sys.argv[:1])

cmdclass = {'test': TestCommand}

version = "%d.%d.%d" % __import__('csvdb').VERSION

classifiers = [
    'Development Status :: 4 - Beta',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Topic :: Database',
]

setup(
    name="csvdb",
    version=version,
    url='https://github.com/nakagami/csvdb/',
    classifiers=classifiers,
    keywords=['csv'],
    author='Hajime Nakagami',
    author_email='nakagami@gmail.com',
    description='Csv data access package like PEP 249 api.',
    license="MIT",
    packages=['csvdb'],
    cmdclass=cmdclass,
)
