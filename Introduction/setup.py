#  Author: Rohan Singh
#  1/6/2023
#  Setup file to demonstrate Hello

#  Imports
from setuptools import setup
from Cython.Build import cythonize

#  Setup
setup(
    name='Hello world app',
    ext_modules=cythonize("hello.pyx"),
    zip_safe=False,
)