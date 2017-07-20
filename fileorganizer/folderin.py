#!/usr/bin/python
""" folderin.py

"""
import os
import logging
import shutil
from _transaction import Transaction
import _helper
from _helper import find_matches_exclude

__author__ = "Jack Chang <wei0831@gmail.com>"

DESCRIPTION = "Put files into folder with the same name"


def _folderin(work_dir):
    matches = find_matches_exclude(0, None, work_dir)

    for files in matches:
        form_dir = os.path.join(work_dir, files)
        to_dir = os.path.join(work_dir, os.path.splitext(files)[0], files)
        yield Transaction(form_dir, to_dir, "move")


def folderin(work_dir, dryrun=True):
    """ Put files into folder with the same name

    Args:
        work_dir (str): Working Directory
        dryrun (bool, optional): Test Run or not
    """
    this_name = folderin.__name__
    loger = logging.getLogger(this_name)

    loger.info("Files will be moved to infividual folders in \"%s\"", work_dir)
    loger.info("=== %s [%s RUN] start ===", this_name, "DRY"
               if dryrun else "WET")

    for item in _folderin(work_dir):
        if not dryrun:
            item.commit()
        else:
            loger.info("%s", item)

    loger.info("=== %s End ===", this_name)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument("workDir", help="Working Directory")
    parser.add_argument(
        "-w",
        "--wetrun",
        action="store_true",
        help="Disable dryrun and Commit changes")
    args = parser.parse_args()

    _helper.init_loger()

    folderin(args.workDir, not args.wetrun)
