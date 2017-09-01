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
    install_requires=[
        'click>=4.0',
    ],
    entry_points={
        'console_scripts': [
            'folderin=fileorganizer.folderin:folderin',
            'folderout=fileorganizer.folderout:folderout',
            'moveintofolder=fileorganizer.moveintofolder:moveintofolder',
            'replacename=fileorganizer.replacename:replacename',
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
