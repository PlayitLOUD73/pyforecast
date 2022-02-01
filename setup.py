from setuptools import setup, find_packages
from sys import platform
import os

with open('requirements.txt', 'r') as req_fp:
    required_packages = req_fp.readlines()

# Use README for long description
with open('README.md', 'r') as readme_fp:
    long_description = readme_fp.read()

setup(
    name="pyforecast",
    version="0.0.1",
    author="Luke Welborn",
    author_email="github@lukewelborn.com",
    description="A simple weather program in the terminal",
    license="",
    keywords="",
    url="https://github.com/PlayitLOUD73/pyforecast",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages = find_packages(exclude=['tests', 'docs']),
    extras_require={
        'test': ['pytest'],
    },
    entry_points={
        'console_scripts': [
            'pyforecast = pyforecast:main',
        ],
    },
    install_requires=required_packages,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],

)