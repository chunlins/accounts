# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='accounts',
    version='0.1.0',
    description='Manage your accounts on comfortable way',
    long_description=readme,
    author='Chunlin Liu',
    author_email='chunlins@outlook.com',
    url='',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=[
        'Click',
    ],
    entry_points="""
        [console_scripts]
        accounts=accounts.interface:accounts
    """,
)
