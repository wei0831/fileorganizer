#!/usr/bin/python
""" folderout.py

"""
import os
import logging
import shutil

__author__ = "Jack Chang <wei0831@gmail.com>"

DESCRIPTION = "Move files out of folders"


def folderout(work_dir, to_dir=None, dryrun=True):
    """ Move files out of folders

    Args:
        work_dir (str): Working Directory
        to_dir (str): Move to Target Directory
        dryrun (bool, optional): Test Run or not
    """
    if work_dir.endswith('\\'):
        work_dir = work_dir[:-1]
    if not to_dir:
        to_dir = work_dir

    loger = logging.getLogger(__name__)
    loger.info("=== %s Start ===", folderout.__name__)
    loger.info("[%s RUN] Move files out of folders in \"%s\" to \"%s\"", "DRY"
               if dryrun else "WET", work_dir, to_dir)

    if not os.path.lexists(to_dir) and not dryrun:
        os.mkdir(to_dir)
        loger.info("New folder created: %s", to_dir)

    folders = [
        f for f in os.listdir(work_dir)
        if os.path.isdir(os.path.join(work_dir, f))
    ]
    to_work = []
    not_work = []

    folders_len = len(folders)
    if folders_len:
        loger.info("[%s folders] to work in %s:", folders_len, work_dir)

        for folder in folders:
            for i in os.listdir(os.path.join(work_dir, folder)):
                to_work.append([folder, i])

    if len(to_work):
        loger.info("[%s items] to work:", len(to_work))

        for i in to_work:
            oldpath = os.path.join(work_dir, *i)
            newpath = os.path.join(to_dir, i[1])

            if os.path.lexists(newpath):
                not_work.append(i)
            else:
                loger.info("%s -> %s", oldpath, newpath)
                if not dryrun:
                    shutil.move(oldpath, newpath)

    not_work_len = len(not_work)
    if not_work_len:
        loger.warning("[%s items] did not work", not_work_len)

        for i in not_work:
            oldpath = os.path.join(work_dir, *i)
            newpath = os.path.join(to_dir, i[1])
            loger.warning("%s -> %s", oldpath, newpath)
            # TODO: figure out what to do next

    if not dryrun:
        for folder in folders:
            checkpath = os.path.join(work_dir, folder)
            if not os.listdir(checkpath):
                os.rmdir(checkpath)
                loger.info("Removed Empty Folder %s", folder)

    loger.info("=== %s End ===", folderout.__name__)


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
