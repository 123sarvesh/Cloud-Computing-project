import os
from   os.path import exists, join, abspath, dirname
from   setuptools import setup

here = abspath(dirname(__file__))

requirements = []
if exists(join(here, 'requirements.txt')):
    with open(join(here, 'requirements.txt')) as f:
        requirements = f.read().rstrip().splitlines()

setup(
    setup_requires = ['wheel'],
    install_requires = requirements,
)
