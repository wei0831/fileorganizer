#!/usr/bin/env python
""" setup.py

"""
from setuptools import setup, find_packages
import fileorganizer

setup(
    name="fileorganizer",
    version=fileorganizer.VERSION,
    packages=find_packages(),
    include_package_data=True,
    install_requires=['click>=6.0', 'yapf>=0.17', 'PyYAML'],
    entry_points={
        'console_scripts': [
            'folderin=fileorganizer.cli:cli_folderin',
            'folderout=fileorganizer.cli:cli_folderout',
            'moveintofolder=fileorganizer.cli:cli_moveintofolder',
            'replacename=fileorganizer.cli:cli_replacename',
            'fanhaorename=fileorganizer.cli:cli_fanhaorename',
            'fanhaofolderin=fileorganizer.cli:cli_fanhaofolderin',
            'renameafterfolder=fileorganizer.cli:cli_renameafterfolder',
        ],
    },
    package_data={
        '': ['*.txt', '*.rst', '*.sh', 'LICENSE', '*md'],
        'fileorganizer': ['conf/*.yaml'],
    },

    # metadata
    author="Jack Chang",
    author_email="wei0831@gmail.com",
    description="batch file organizer",
    license="MIT",
    keywords="file organizer",
    url="https://github.com/wei0831/fileorganizer",
    classifiers=[
        'Development Status :: 1 - Planning Development',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ], )
