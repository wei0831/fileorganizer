#!/usr/bin/python
""" folderin.py

"""
import os
import logging
import shutil
import re

__author__ = "Jack Chang <wei0831@gmail.com>"

DESCRIPTION = "Put files into folder with the same name"


def folderin(work_dir, dryrun=True):
    """ Put files into folder with the same name

    Args:
        work_dir (str): Working Directory
        dryrun (bool, optional): Test Run or not
    """
    if work_dir.endwith('\\'):
        work_dir = work_dir[:-1]

    loger = logging.getLogger(__name__)
    loger.info("=== %s Start ===", folderin.__name__)
    loger.info("[%s RUN] Files will be moved to infividual folders in \"%s\"",
               "DRY" if dryrun else "WET", work_dir)

    to_work = [
        f for f in os.listdir(work_dir)
        if os.path.isfile(os.path.join(work_dir, f))
    ]
    not_work = []

    to_work_len = len(to_work)
    if to_work_len:
        loger.info("[%s items] to work in %s:", to_work_len, work_dir)

        for f in to_work:
            foldername = os.path.splitext(f)[0]
            newfolderpath = os.path.join(work_dir, foldername)

            if not dryrun and not os.path.exists(newfolderpath):
                os.mkdir(newfolderpath)
                loger.info("New folder created: %s", newfolderpath)

            oldfilepath = os.path.join(work_dir, f)
            newfilepath = os.path.join(newfolderpath, f)
            loger.info("%s -> %s", oldfilepath, newfilepath)

            if not dryrun:
                if os.path.isfile(newfilepath):
                    not_work.append([oldfilepath, newfilepath])
                else:
                    shutil.move(oldfilepath, newfilepath)

    not_work_len = len(not_work)
    if not_work_len:
        loger.warning("[%s items] did not work in %s:", not_work_len, work_dir)

        for f in not_work:
            loger.warning("%s -> %s", f[0], f[1])
            # TODO: figure out what to do next

    loger.info("=== %s End ===", folderin.__name__)


if __name__ == "__main__":
    import helper
    import argparse
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument("workDir", help="Working Directory")
    parser.add_argument(
        "-w",
        "--wetrun",
        action="store_true",
        help="Disable dryrun and Commit changes")
    args = parser.parse_args()

    helper.init_loger()

    folderin(args.workDir, not args.wetrun)
