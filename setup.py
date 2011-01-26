#!/usr/bin/env python
try:
    from setuptools import setup
except:
    from distutils.core import setup

setup(name='pyGravatar',
      version='0.0.5',
      description='Python module for interacting with Gravatar',
      author='Eric Seidel',
      author_email='gridaphobe@gmail.com',
      url='http://bitbucket.org/gridaphobe/pygravatar',
      py_modules=['gravatar'],
      license='GPL',
      keywords='gravatar',
      )