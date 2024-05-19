"""
setup.py configuration script describing how to build and package this project.

This file is primarily used by the setuptools library and typically should not
be executed directly. See README.md for how to deploy, test, and run
the project1 project.
"""
from setuptools import setup, find_packages

import sys
sys.path.append('./src')

import datetime
import project1

setup(
    name="project1",
    # We use timestamp as Local version identifier (https://peps.python.org/pep-0440/#local-version-identifiers.)
    # to ensure that changes to wheel package are picked up when used on all-purpose clusters
    version=project1.__version__ + "+" + datetime.datetime.utcnow().strftime("%Y%m%d.%H%M%S"),
    url="https://databricks.com",
    author="d46cd08f-cbea-4b56-81b9-e2e36ed96e37",
    packages=find_packages(where='./wheel'),
    package_dir={'': 'wheel'},
    entry_points={
        "packages": [
            "main=project1.main:main"
        ]
    },
    install_requires=[
        # Dependencies in case the output wheel file is used as a library dependency.
        # For defining dependencies, when this package is used in Databricks, see:
        # https://docs.databricks.com/dev-tools/bundles/library-dependencies.html
        "setuptools"
    ],
)
