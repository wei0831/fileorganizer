#!/usr/bin/python
""" replacename.py

"""
import os
import os.path
import re
import logging
import fileorganizer
from fileorganizer import _helper
from fileorganizer._helper import find_matches_exclude
from fileorganizer._transaction import Transaction

__author__ = "Jack Chang <wei0831@gmail.com>"

DESCRIPTION = "Find string in File name/Folder name and replace with another string"


def _replacename(find, replace, work_dir, mode=0, exclude=None):
    regex_find = re.compile(find)
    matches = find_matches_exclude(mode, find, work_dir, exclude)
    get_newname = lambda f: regex_find.sub(replace, f)

    for oldname in matches:
        newname = get_newname(oldname)

        if not newname == oldname and not newname == "":
            oldnamepath = os.path.join(work_dir, oldname)
            newnamepath = os.path.join(work_dir, newname)

            yield Transaction(oldnamepath, newnamepath, "mv")


def replacename(find,
                replace,
                work_dir,
                exclude=None,
                mode=0,
                wetrun=False,
                this_name=os.path.basename(__file__)):
    """ Find string in File name/Folder name and replace with another string

    \b
    Args:
        find (str): Regex string to find in filename/foldername
        replace (str): Regex string to replace in filename/foldername
        work_dir (str): Working Directory
        exclude (str, optional): Regex string to exclude in mattches
        mode (int, optional): 0=FILE ONLY, 1=FOLDER ONLY, 2=BOTH
        wetrun (bool, optional): Test Run or not
        this_name (str, optional): caller name
    """
    _helper.init_loger()
    this_run = "WET" if wetrun else "DRY"
    loger = logging.getLogger(this_name)
    loger.info("[START] === %s [%s RUN] ===", this_name, this_run)
    loger.info("[DO] Replace \"%s\" with \"%s\" in \"%s\"; Mode %s", find,
               replace, work_dir, mode)

    for item in _replacename(find, replace, work_dir, mode, exclude):
        if wetrun:
            item.commit()
        else:
            loger.info("%s", item)

    loger.info("[END] === %s [%s RUN] ===", this_name, this_run)


if __name__ == "__main__":
    fileorganizer.cli.cli_replacename()
