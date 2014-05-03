#!/usr/bin/env python
try:
    from setuptools import setup
except:
    from distutils.core import setup

setup(name='pyGravatar',
      version='0.0.6',
      description='Python module for interacting with Gravatar',
      author='Eric Seidel',
      author_email='gridaphobe@gmail.com',
      url='https://github.com/gridaphobe/pyGravatar',
      py_modules=['gravatar'],
      license='GPL',
      keywords='gravatar',
      )
