#!/usr/bin/python
""" helper.py

This module contains several helper functions
"""
import os
import logging
import logging.config
import yaml

__author__ = "Jack Chang <wei0831@gmail.com>"


def init_loger(path='conf\\logging.yaml', default_level=logging.INFO):
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
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())

        logging.config.dictConfig(config)
        logging.getLogger(__name__).debug("Config '%s' is loaded.", path)
    else:
        logging.basicConfig(level=default_level)
