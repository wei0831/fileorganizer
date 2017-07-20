#!/usr/bin/python
""" replacename.py

"""
import os
import os.path
import re
import logging
import _helper
from _helper import find_matches_exclude
from _transaction import Transaction

__author__ = "Jack Chang <wei0831@gmail.com>"

DESCRIPTION = "Find string in File name/Folder name and replace with another string"


def _replacename(find, replace, work_dir, mode=0, exclude=None):
    regex_find = re.compile(find)
    matches = find_matches_exclude(mode, find, work_dir, exclude)
    get_newname = lambda f: regex_find.sub(replace, f)

    for oldname in matches:
        newname = get_newname(oldname)

        if not newname == oldname:
            oldnamepath = os.path.join(work_dir, oldname)
            newnamepath = os.path.join(work_dir, newname)

            yield Transaction(oldnamepath, newnamepath, "move")


def replacename(find, replace, work_dir, exclude=None, dryrun=True, mode=0):
    """ Find string in File name/Folder name and replace with another string

    Args:
        find (str): Regex string to find in filename/foldername
        replace (str): Regex string to replace in filename/foldername
        work_dir (str): Working Directory
        exclude (str): Regex string to exclude in mattches
        dryrun (bool, optional): Test Run or not
        mode (int, optional): 0=FILE ONLY, 1=FOLDER ONLY, 2=BOTH
    """
    this_name = replacename.__name__
    loger = logging.getLogger(this_name)
    loger.info("Replace \"%s\" with \"%s\" in \"%s\" [Mode %s]", find, replace,
               work_dir, mode)
    loger.info("=== %s [%s RUN] start ===", this_name, "DRY"
               if dryrun else "WET")

    for item in replacename(find, replace, work_dir, mode, exclude):
        if not dryrun:
            item.commit()
        loger.info("%s", item)

    loger.info("=== %s end ===")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument(
        "find", help="String to Replace in filename/foldername")
    parser.add_argument(
        "replace", help="To Replace With in filename/foldername")
    parser.add_argument("-e", "--exclude", help="Exclude regex pattern")
    parser.add_argument("-d", "--dir", help="Working Directory")
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

    replacename(args.find, args.replace, args.dir if args.dir else os.getcwd(),
                args.exclude, not args.wetrun, args.mode)
