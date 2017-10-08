#!/usr/bin/python
""" _helper.py

This module contains several helper functions
"""
import errno
import os
import stat
import logging
import logging.config
import re
import yaml

__author__ = "Jack Chang <wei0831@gmail.com>"


def init_loger(path=os.path.join(
        os.path.dirname(os.path.realpath(__file__)), 'conf/logging.yaml'),
               default_level=logging.INFO):
    """ Initialize Logging Module
    Note:
        If config file is not present, the basic config with default_level is set.
    Args:
        path (str, optional): path to .yaml config file
        default_level (int, optional): logging level
    """
    if os.path.exists(path):
        with open(path, 'rt') as config:
            config = yaml.safe_load(config.read())

        if not os.path.exists('fo_log'):
            os.mkdir('fo_log')

        logging.config.dictConfig(config)
        logging.getLogger(__name__).info("Config '%s' is loaded.", path)
    else:
        logging.basicConfig(level=default_level)
        logging.getLogger(__name__).info("Default Config is loaded.")


FILEONLY = 0
FOLDERONLY = 1
BOTHFILEFOLDER = 2


def find_matches_exclude(mode,
                         find,
                         work_dir,
                         exclude=None,
                         casesensitive=True):
    """ TODO
    """
    check_mode = lambda f: True
    check_match = lambda f: True
    check_exclude = lambda f: False

    if casesensitive:
        if mode == FILEONLY:
            check_mode = lambda f: os.path.isfile(os.path.join(work_dir, f))
        elif mode == FOLDERONLY:
            check_mode = lambda f: os.path.isdir(os.path.join(work_dir, f))
        elif mode == BOTHFILEFOLDER:
            check_mode = lambda f: os.path.exists(os.path.join(work_dir, f))
    else:
        if mode == FILEONLY:
            check_mode = lambda f: f.lower() in [i.lower() for i in os.listdir(work_dir) if os.path.isfile(os.path.join(work_dir, i))]
        elif mode == FOLDERONLY:
            check_mode = lambda f: f.lower() in [i.lower() for i in os.listdir(work_dir) if os.path.isdir(os.path.join(work_dir, i))]
        elif mode == BOTHFILEFOLDER:
            check_mode = lambda f: f.lower() in [i.lower() for i in os.listdir(work_dir)]

    if find is not None:
        regex_find = re.compile(
            find, flags=re.IGNORECASE if not casesensitive else 0)
        check_match = lambda f: regex_find.search(f) is not None

    if exclude:
        regex_exlude = re.compile(
            exclude, flags=re.IGNORECASE if not casesensitive else 0)
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
