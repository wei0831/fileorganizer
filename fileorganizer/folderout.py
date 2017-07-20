#!/usr/bin/python
""" folderout.py

"""
import os
import logging
import shutil
from _transaction import Transaction
from _helper import find_matches_exclude

__author__ = "Jack Chang <wei0831@gmail.com>"

DESCRIPTION = "Move files out of folders"


def _folderout(work_dir, to_dir):
    matches = find_matches_exclude(1, None, work_dir)

    dir_towork = []

    for folder in matches:
        old_dir = os.path.join(work_dir, folder)
        dir_towork.append(old_dir)
        for item in os.listdir(old_dir):
            old_path = os.path.join(old_dir, item)
            new_path = os.path.join(to_dir, item)
            yield Transaction(old_path, new_path, "move")

    for folder in dir_towork:
        yield Transaction(folder, None, "rmdir")


def folderout(work_dir, to_dir=None, dryrun=True):
    """ Move files out of folders

    Args:
        work_dir (str): Working Directory
        to_dir (str): Move to Target Directory
        dryrun (bool, optional): Test Run or not
    """
    this_name = folderout.__name__
    loger = logging.getLogger(this_name)
    loger.info("Move files out of folders in \"%s\" to \"%s\"", work_dir,
               to_dir)
    loger.info("=== %s [%s RUN] start ===", folderout.__name__, "DRY"
               if dryrun else "WET")

    for item in _folderout(work_dir, to_dir
                           if to_dir is not None else work_dir):
        if not dryrun:
            item.commit()
        loger.info("%s", item)

    loger.info("=== %s End ===", this_name)


if __name__ == "__main__":
    import _helper
    import argparse
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument("workDir", help="Working Directory")
    parser.add_argument("-t", "--to", default=None, help="Target Directory")
    parser.add_argument(
        "-w",
        "--wetrun",
        action="store_true",
        help="Disable dryrun and Commit changes")
    args = parser.parse_args()

    _helper.init_loger()

    folderout(args.workDir, args.to, not args.wetrun)
