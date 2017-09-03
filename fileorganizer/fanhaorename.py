#!/usr/bin/python
""" fanhaorename.py

"""
import os
import os.path
import fileorganizer
from fileorganizer.replacename import replacename

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
                 find=None,
                 replace=None,
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
    _find = r"(.*)({0})(-|_| )*(\d\d\d)(.*)(\.(.*))"
    _replace = r"{0}-\4\6"

    if not find:
        find = _find.format(_tagHelper(tag))
    if not replace:
        replace = _replace.format(tag)

    replacename(find, replace, work_dir, exclude, mode, wetrun, this_name)


if __name__ == "__main__":
    fileorganizer.cli.cli_fanhaorename()
