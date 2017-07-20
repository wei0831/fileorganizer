#!/usr/bin/python
""" _helper.py

This module contains several helper functions
"""
import os
import logging
import logging.config
import re
import yaml

__author__ = "Jack Chang <wei0831@gmail.com>"


def init_loger(path=os.path.dirname(os.path.realpath(__file__)) +
               '\\conf\\logging.yaml',
               default_level=logging.INFO):
    """ Initialize Logging Module
    Note:
        If config file is not present, the basic config with default_level is set.
    Args:
        path (str, optional): path to .yaml config file
        default_level (int, optional): logging level
    """
    if not os.path.exists('log'):
        os.mkdir('log')

    if os.path.exists(path):
        with open(path, 'rt') as config:
            config = yaml.safe_load(config.read())

        logging.config.dictConfig(config)
        logging.getLogger(__name__).debug("Config '%s' is loaded.", path)
    else:
        logging.basicConfig(level=default_level)


FILEONLY = 0
FOLDERONLY = 1
BOTHFILEFOLDER = 2


def find_matches_exclude(mode, find, work_dir, exclude=None):
    """ TODO
    """
    check_mode = lambda f: True
    if mode == FILEONLY:
        check_mode = lambda f: os.path.isfile(os.path.join(work_dir, f))
    elif mode == FOLDERONLY:
        check_mode = lambda f: os.path.isdir(os.path.join(work_dir, f))

    check_match = lambda f: True
    if find is not None:
        regex_find = re.compile(find)
        check_match = lambda f: regex_find.search(f) is not None

    check_exclude = lambda f: False
    if exclude:
        regex_exlude = re.compile(exclude)
        check_exclude = lambda f: regex_exlude.search(f) is not None

    for item in os.listdir(work_dir):
        if check_mode(item) and not check_exclude(item) and check_match(item):
            yield item
