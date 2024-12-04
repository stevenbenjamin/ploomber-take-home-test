import re
import ast
from glob import glob
from os.path import basename, splitext

from setuptools import find_packages
from setuptools import setup

_version_re = re.compile(r"__version__\s+=\s+(.*)")

with open("src/ploomber_test/__init__.py", "rb") as f:
    VERSION = str(
        ast.literal_eval(_version_re.search(f.read().decode("utf-8")).group(1))
    )

REQUIRES = [
    "mistune==3.0.2",
    "duckdb==0.8.1",
    "ipython==8.25.0",
    "click==8.1.7",
]

DEV = [
    "pytest==7.4.4",
    "build==0.10.0",
    "invoke==2.2.0",
    "flake8==7.1.0",
]

setup(
    name="ploomber-test",
    version=VERSION,
    description=None,
    license=None,
    author=None,
    author_email=None,
    url=None,
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(path))[0] for path in glob("src/*.py")],
    include_package_data=True,
    classifiers=[],
    keywords=[],
    install_requires=REQUIRES + DEV,
    entry_points={
        "console_scripts": ["ploomber-test=ploomber_test.cli:cli"],
    },
)
