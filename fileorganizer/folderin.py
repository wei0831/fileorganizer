#!/usr/bin/python
""" folderin.py

"""
import os
import logging
import fileorganizer
from fileorganizer import _helper
from fileorganizer._transaction import Transaction
from fileorganizer._helper import find_matches_exclude

__author__ = "Jack Chang <wei0831@gmail.com>"

DESCRIPTION = "Put files into folder with the same name"


def _folderin(work_dir):
    matches = find_matches_exclude(0, None, work_dir)

    for files in matches:
        form_dir = os.path.join(work_dir, files)
        to_dir = os.path.join(work_dir, os.path.splitext(files)[0], files)
        yield Transaction(form_dir, to_dir, "mv")


def folderin(work_dir, wetrun=False, this_name=os.path.basename(__file__)):
    """ Put files into folder with the same name

    \b
    Args:
      work_dir (str): Working Directory
      wetrun (bool, optional): Test Run or not
    """
    _helper.init_loger()
    this_run = "WET" if wetrun else "DRY"
    loger = logging.getLogger(this_name)
    loger.info("[START] === %s [%s RUN] ===", this_name, this_run)
    loger.info("[DO] Files move to individual folders in \"%s\"", work_dir)

    for item in _folderin(work_dir):
        if wetrun:
            item.commit()
        else:
            loger.info("%s", item)

    loger.info("[END] === %s [%s RUN] ===", this_name, this_run)


if __name__ == "__main__":
    fileorganizer.cli.cli_folderin()
