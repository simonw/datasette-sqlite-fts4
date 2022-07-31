from setuptools import setup
import os

VERSION = "0.3.2"


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
    project_urls={
        "Issues": "https://github.com/simonw/datasette-sqlite-fts4/issues",
        "CI": "https://github.com/simonw/datasette-sqlite-fts4/actions",
        "Changelog": "https://github.com/simonw/datasette-sqlite-fts4/releases",
    },
    license="Apache License, Version 2.0",
    classifiers=[
        "Framework :: Datasette",
        "License :: OSI Approved :: Apache Software License",
    ],
    version=VERSION,
    packages=["datasette_sqlite_fts4"],
    entry_points={"datasette": ["sqlite_fts4 = datasette_sqlite_fts4"]},
    install_requires=["datasette", "sqlite-fts4>=1.0.3"],
    extras_require={"test": ["pytest", "pytest-asyncio"]},
    python_requires=">=3.7",
)
