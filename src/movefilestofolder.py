#!/usr/bin/python
""" movefilestofolder.py

"""
import os
import logging
import shutil
import re

__author__ = "Jack Chang <wei0831@gmail.com>"

DESCRIPTION = "Move matching files into a folder"


def movefilestofolder(find, work_dir, to_dir, dryrun=True):
    """ Move matching files into a folder

    Args:
        find (str): Regex String to find matching files
        work_dir (str): Working Directory
        to_dir (str): Move to Target Directory
        dryrun (bool, optional): Test Run or not
    """
    if to_dir.startswith("./"):
        to_dir = work_dir + '//' + to_dir[2:]
    if to_dir.startswith(".\\"):
        to_dir = work_dir + '\\' + to_dir[2:]

    loger = logging.getLogger(__name__)
    loger.info("=== %s Start ===", movefilestofolder.__name__)
    loger.info(
        "[%s RUN] Files matches \"%s\" in \"%s\" will be moved to \"%s\"",
        "DRY" if dryrun else "WET", find, work_dir, to_dir)

    find_regex = re.compile(find)
    to_work = [
        f for f in os.listdir(work_dir)
        if os.path.isfile(os.path.join(work_dir, f)) and find_regex.match(f) is
        not None
    ]
    not_work = []

    to_work_len = len(to_work)
    if to_work_len:
        loger.info("[%s items] to work in %s:", to_work_len, work_dir)
        if not dryrun and not os.path.exists(to_dir):
            os.mkdir(to_dir)
            loger.info("New folder created at %s:", to_dir)

        for f in to_work:
            oldfilepath = os.path.join(work_dir, f)
            newfilepath = os.path.join(to_dir, f)

            if os.path.isfile(newfilepath):
                not_work.append([oldfilepath, newfilepath])
            else:
                loger.info("%s -> %s", oldfilepath, newfilepath)
                if not dryrun:
                    shutil.move(oldfilepath, newfilepath)

    not_work_len = len(not_work)
    if not_work_len:
        loger.warning("[%s items] did not work in %s:", not_work_len, work_dir)

        for f in not_work:
            loger.warning("%s -> %s", f[0], f[1])
            # TODO: figure out what to do next

    loger.info("=== %s End ===", movefilestofolder.__name__)


if __name__ == "__main__":
    import helper
    import argparse
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument("find", help="Regex string to find matching files")
    parser.add_argument("workDir", help="Working Directory")
    parser.add_argument("toDir", help="Target Directory")
    parser.add_argument(
        "-w",
        "--wetrun",
        action="store_true",
        help="Disable dryrun and Commit changes")
    args = parser.parse_args()

    helper.init_loger()

    movefilestofolder(args.find, args.workDir, args.toDir, not args.wetrun)
