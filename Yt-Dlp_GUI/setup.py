import py2exe
from distutils.core import setup

setup(
    name="YT-DLP GUI",
    windows=["src/controller.py"],
    packages=["src"]
)
