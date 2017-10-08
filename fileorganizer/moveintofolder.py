#!/usr/bin/python
""" moveintofolder.py

"""
import os
import logging
import fileorganizer
from fileorganizer import _helper
from fileorganizer._transaction import Transaction
from fileorganizer._helper import find_matches_exclude

__author__ = "Jack Chang <wei0831@gmail.com>"

DESCRIPTION = "Move matching files/folder into a folder"


def _moveintofolder(find,
                    work_dir,
                    to_dir,
                    exclude=None,
                    mode=0,
                    casesensitive=True):
    matches = find_matches_exclude(mode, find, work_dir, exclude,
                                   casesensitive)

    for item in matches:
        oldnamepath = os.path.join(work_dir, item)
        newnamepath = os.path.join(to_dir, item)

        yield Transaction(oldnamepath, newnamepath, "mv")


def moveintofolder(find,
                   work_dir,
                   to_dir,
                   exclude=None,
                   mode=0,
                   casesensitive=True,
                   wetrun=False,
                   this_name=os.path.basename(__file__)):
    """ Move matching files/folder into a folder

    \b
    Args:
        find (str): Regex string to find in filename/foldername
        work_dir (str): Working Directory
        to_dir (str): Target Directory
        exclude (str, optional): Regex string to exclude in mattches
        mode (int, optional): 0=FILE ONLY, 1=FOLDER ONLY, 2=BOTH
        wetrun (bool, optional): Test Run or not
    """
    _helper.init_loger()
    this_run = "WET" if wetrun else "DRY"
    loger = logging.getLogger(this_name)
    loger.info("[START] === %s [%s RUN] ===", this_name, this_run)
    loger.info(
        "[DO] Matches \"%s\" in \"%s\"; Excludes \"%s\"; Moved to \"%s\"; Mode %s",
        find, work_dir, exclude, to_dir, mode)

    for item in _moveintofolder(find, work_dir, to_dir, exclude, mode,
                                casesensitive):
        if wetrun:
            item.commit()
        else:
            loger.info("%s", item)

    loger.info("[END] === %s [%s RUN] ===", this_name, this_run)


if __name__ == "__main__":
    fileorganizer.cli.cli_moveintofolder()
