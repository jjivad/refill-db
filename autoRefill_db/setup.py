# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='skeleton',
    version='0.1.0',
    description='Sample package for Python-Guide.org',
    long_description=readme,
    author='Hendrik Bitzmann',
    author_email='hendrik.bitzmann@gmail.com',
    url='https://github.com/bizzmane/skeleton',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

