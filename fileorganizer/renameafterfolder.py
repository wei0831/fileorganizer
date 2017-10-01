#!/usr/bin/python
""" renameafterfolder.py

"""
import os
import logging
import fileorganizer
from fileorganizer import _helper
from fileorganizer._transaction import Transaction
from fileorganizer._helper import find_matches_exclude

__author__ = "Jack Chang <wei0831@gmail.com>"

DESCRIPTION = "Rename all files inside folder with folder name"


def _renameafterfolder(find, work_dir, exclude=None):
    matches = find_matches_exclude(_helper.FOLDERONLY, find, work_dir, exclude)

    for foldername in matches:
        todopath = os.path.join(work_dir, foldername)
        for todo in [
                f for f in os.listdir(todopath)
                if os.path.isfile(os.path.join(todopath, f))
        ]:
            oldnamepath = os.path.join(todopath, todo)
            _, todo_ext = os.path.splitext(oldnamepath)
            newnamepath = os.path.join(todopath, foldername + todo_ext)
            if oldnamepath != newnamepath:
                yield Transaction(oldnamepath, newnamepath, "mv")


def renameafterfolder(find,
                      work_dir,
                      exclude=None,
                      wetrun=False,
                      this_name=os.path.basename(__file__)):
    """ Rename all files inside folder with folder name

    \b
    Args:
        find (str): Regex string to find in filename/foldername
        work_dir (str): Working Directory
        exclude (str, optional): Regex string to exclude in mattches
        wetrun (bool, optional): Test Run or not
    """
    _helper.init_loger()
    this_run = "WET" if wetrun else "DRY"
    loger = logging.getLogger(this_name)
    loger.info("[START] === %s [%s RUN] ===", this_name, this_run)
    loger.info("[DO] Matches \"%s\" in \"%s\"; Excludes \"%s\"", find,
               work_dir, exclude)

    for item in _renameafterfolder(find, work_dir, exclude):
        if wetrun:
            item.commit()
        else:
            loger.info("%s", item)

    loger.info("[END] === %s [%s RUN] ===", this_name, this_run)


if __name__ == "__main__":
    fileorganizer.cli.cli_renameafterfolder()
