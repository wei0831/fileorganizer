#!/usr/bin/python
""" fanhaorename.py

"""
import os
import os.path
import logging
import fileorganizer
from fileorganizer import _helper
from fileorganizer.replacename import _replacename

__author__ = "Jack Chang <wei0831@gmail.com>"


def _tagHelper(tag):
    """ TODO
    """
    result = ""
    for c in tag:
        if c.isalpha():
            result += "[{0}{1}]".format(c.lower(), c.upper())
        else:
            result += c
    return result


def fanhaorename(work_dir,
                 tag,
                 exclude=None,
                 mode=0,
                 wetrun=False,
                 this_name=os.path.basename(__file__)):
    """ Batch Rename Fanhao

    \b
    Args:
        work_dir (str): Working Directory
        tag (str): Fanhao tag
        find (str, optional): Regex string to find in filename/foldername
        replace (str, optional): Regex string to replace in filename/foldername
        exclude (str, optional): Regex string to exclude in mattches
        mode (int, optional): 0=FILE ONLY, 1=FOLDER ONLY, 2=BOTH
        wetrun (bool, optional): Test Run or not
    """
    _find_dir = r"(.*)({0})(-|_| )*(\d\d\d)(.*)".format(_tagHelper(tag))
    _replace_dir = r"{0}-\4".format(tag)
    _find_file = _find_dir + r"(\.(.*))"
    _replace_file = _replace_dir + r"\6"

    _helper.init_loger()
    this_run = "WET" if wetrun else "DRY"
    loger = logging.getLogger(this_name)
    loger.info("[START] === %s [%s RUN] ===", this_name, this_run)
    loger.info("[DO] Rename \"%s\" fanhao in \"%s\"; Mode %s", tag, work_dir,
               mode)

    if mode in (0, 2): # mode 0 and 2
        for item in _replacename(_find_file, _replace_file, work_dir, 0,
                                 exclude):
            item.commit() if wetrun else loger.info("%s", item)

    if mode in (1, 2): # mode 1 and 2
        for item in _replacename(_find_dir, _replace_dir, work_dir, 1,
                                 exclude):
            item.commit() if wetrun else loger.info("%s", item)

    loger.info("[END] === %s [%s RUN] ===", this_name, this_run)


if __name__ == "__main__":
    fileorganizer.cli.cli_fanhaorename()
