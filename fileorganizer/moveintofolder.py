#!/usr/bin/python
""" moveintofolder.py

"""
import os
import logging
from _transaction import Transaction
from _helper import find_matches_exclude

__author__ = "Jack Chang <wei0831@gmail.com>"

DESCRIPTION = "Move matching files/folder into a folder"


def _moveintofolder(find, work_dir, to_dir, exclude=None, mode=0):
    matches = find_matches_exclude(mode, find, work_dir, exclude)

    for item in matches:
        oldnamepath = os.path.join(work_dir, item)
        newnamepath = os.path.join(to_dir, item)

        yield Transaction(oldnamepath, newnamepath, "move")


def moveintofolder(find, work_dir, to_dir, exclude=None, dryrun=True, mode=0):
    """ Move matching files/folder into a folder

    Args:
        find (str): Regex String to find matching files
        work_dir (str): Working Directory
        to_dir (str): Move to Target Directory
        dryrun (bool, optional): Test Run or not
    """
    this_name = moveintofolder.__name__
    loger = logging.getLogger(this_name)
    loger.info("Files matches \"%s\" in \"%s\" will be moved to \"%s\"", find,
               work_dir, to_dir)
    loger.info("=== %s [%s RUN] start ===", this_name, "DRY"
               if dryrun else "WET")

    for item in _moveintofolder(find, work_dir, to_dir, exclude, mode):
        if not dryrun:
            item.commit()
        else:
            loger.info("%s", item)

    loger.info("=== %s End ===", this_name)


if __name__ == "__main__":
    import _helper
    import argparse
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument("find", help="Regex string to find matching files")
    parser.add_argument("workDir", help="Working Directory")
    parser.add_argument("toDir", help="Target Directory")
    parser.add_argument("-e", "--exclude", help="Exclude regex pattern")
    parser.add_argument(
        "-m",
        "--mode",
        type=int,
        default=0,
        help="0: FILE_ONLY, 1: FOLDER_ONLY, 2: BOTH")
    parser.add_argument(
        "-w",
        "--wetrun",
        action="store_true",
        help="Disable dryrun and Commit changes")
    args = parser.parse_args()

    _helper.init_loger()

    moveintofolder(args.find, args.workDir, args.toDir, args.exclude,
                   not args.wetrun, args.mode)
