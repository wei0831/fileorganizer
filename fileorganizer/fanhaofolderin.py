#!/usr/bin/python
""" fanhaofolderin.py

"""
import os
import logging
import fileorganizer
from fileorganizer import _helper
from fileorganizer._transaction import Transaction
from fileorganizer._helper import find_matches_exclude

__author__ = "Jack Chang <wei0831@gmail.com>"

DESCRIPTION = "Organize file XXX-YYY into folder XXX"


def _fanhaofolderin(work_dir):
    matches = find_matches_exclude(0, "-", work_dir)

    for files in matches:
        form_dir = os.path.join(work_dir, files)
        to_dir = os.path.join(work_dir, files.split("-")[0], files)
        yield Transaction(form_dir, to_dir, "mv")


def fanhaofolderin(work_dir, wetrun=False, this_name=os.path.basename(__file__)):
    """ Organize file XXX-YYY into folder XXX

    \b
    Args:
      work_dir (str): Working Directory
      wetrun (bool, optional): Test Run or not
    """
    _helper.init_loger()
    this_run = "WET" if wetrun else "DRY"
    loger = logging.getLogger(this_name)
    loger.info("[START] === %s [%s RUN] ===", this_name, this_run)
    loger.info("[DO] Work Directory: \"%s\"", work_dir)

    for item in _fanhaofolderin(work_dir):
        if wetrun:
            item.commit()
        else:
            loger.info("%s", item)

    loger.info("[END] === %s [%s RUN] ===", this_name, this_run)


if __name__ == "__main__":
    fileorganizer.cli.cli_fanhaofolderin()
