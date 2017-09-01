#!/usr/bin/python
""" _helper.py

This module contains several helper functions
"""
import errno
import os
import stat
import shutil
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
    if not os.path.exists('fo_log'):
        os.mkdir('fo_log')

    if os.path.exists(path):
        with open(path, 'rt') as config:
            config = yaml.safe_load(config.read())

        logging.config.dictConfig(config)
        logging.getLogger(__name__).debug("Config '%s' is loaded.", path)
    else:
        logging.basicConfig(level=default_level)
        logging.getLogger(__name__).debug("Default Config is loaded.", path)


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


def handleRemoveReadonly(func, path, exc):
    """ TODO
    """
    excvalue = exc[1]
    if func in (os.rmdir, os.remove) and excvalue.errno == errno.EACCES:
        os.chmod(path, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)  # 0777
        func(path)
