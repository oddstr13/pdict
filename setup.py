# -*- coding: utf-8 -*-
from setuptools import setup

with open("README.md", 'r') as fh:
    long_description = fh.read()

setup(
   name = 'pdict',
   version = '1.0',
   description = 'Provides PersistentDict, a dictionary with save and load functions.',
   license = "MIT",
   long_description = long_description,
   author = 'Odd Stråbø',
   author_email = 'oddstr13@openshell.no',
   url = "https://github.com/oddstr13",
   packages = ['pdict']
)