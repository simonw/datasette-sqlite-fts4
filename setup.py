from setuptools import setup
import os

VERSION = "0.3.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="datasette-sqlite-fts4",
    description="Datasette plugin exposing SQL functions from sqlite-fts4",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    url="https://github.com/simonw/datasette-sqlite-fts4",
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["datasette_sqlite_fts4"],
    entry_points={"datasette": ["sqlite_fts4 = datasette_sqlite_fts4"]},
    install_requires=["datasette", "sqlite-fts4>=1.0.2"],
)
