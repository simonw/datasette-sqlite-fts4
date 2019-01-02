from setuptools import setup

VERSION = '0.2'

setup(
    name='datasette-sqlite-fts4',
    description='Custom SQL functions for working with SQLite FTS4',
    author='Simon Willison',
    url='https://github.com/simonw/datasette-sqlite-fts4',
    license='Apache License, Version 2.0',
    version=VERSION,
    packages=['datasette_sqlite_fts4'],
    entry_points={
        'datasette': [
            'sqlite_fts4 = datasette_sqlite_fts4'
        ]
    },
    install_requires=['datasette', 'sqlite-fts4']
)
