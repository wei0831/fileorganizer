import os
import sys
import shutil
import re
import logging

FILEONLY = 0
FOLDERONLY = 1
BOTHFILEFOLDER = 2
DESCRIPTION = "Find string in File name/Folder name and replace with another string"


def replacename(find, replace, work_dir, dryrun=True, mode=0, regex=False):
    """ Find string in File name/Folder name and replace with another string

    Args:
        find (str): String to find in filename/foldername
        replace (str): To replace with in filename/foldername
        work_dir (str): Working Directory
        dryrun (bool, optional): Test Run or not
        mode (int, optional): 0=FILE ONLY, 1=FOLDER ONLY, 2=BOTH
        regex (bool, optional): Treat input string as regex
    """
    loger = logging.getLogger(__name__)
    loger.info("=== {} Start ===".format(replacename.__name__))
    loger.info("[{} RUN][Mode {}] Replace \"{}\" with \"{}\" in \"{}\"".format(
        "DRY" if dryrun else "WET", mode, find, replace, work_dir))

    if mode == FILEONLY:
        checkmode = lambda f: os.path.isfile(os.path.join(work_dir, f))
    elif mode == FOLDERONLY:
        checkmode = lambda f: os.path.isdir(os.path.join(work_dir, f))
    elif mode == BOTHFILEFOLDER:
        checkmode = lambda f: True

    if regex:
        find_regex = re.compile(find)
        checkmatch = lambda f: find_regex(f) is not None
        getnewfilename = lambda f: find_regex(replace, f)
    else:
        checkmatch = lambda f: find in f
        getnewfilename = lambda f: f.replace(find, replace)

    matches = [
        f for f in os.listdir(work_dir) if checkmode(f) and checkmatch(f)
    ]

    to_work = []
    not_work = []
    for f in matches:
        newfilename = getnewfilename(f)
        newfilename = os.path.splitext(newfilename)[0] + os.path.splitext(
            newfilename)[1]

        if not newfilename == f:
            to_work.append([f, newfilename])

    to_work_len = len(to_work)
    if to_work_len:
        loger.info("[{} items] to work:".format(to_work_len))

        for f in to_work:
            loger.info("{} -> {}".format(f[0], f[1]))
            if not dryrun:
                if f[1] in os.listdir(work_dir):
                    not_work.append([f, f[1]])
                else:
                    newfilepath = os.path.join(work_dir, f[1])
                    shutil.move(os.path.join(work_dir, f[0]), newfilepath)

    not_work_len = len(not_work)
    if not_work_len:
        loger.info("[{} items] did not work:".format(not_work_len))

        for f in not_work:
            if dryrun:
                loger.info("{} -> {}".format(f[0], f[1]))

    loger.info("=== {} End ===".format(replacename.__name__))


if __name__ == "__main__":
    import helper
    import argparse
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument(
        "find",
        metavar="Find",
        help="String to Replace in filename/foldername")
    parser.add_argument(
        "replace",
        metavar="ReplaceWith",
        help="To Replace With in filename/foldername")
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
    parser.add_argument(
        "-r",
        "--regex",
        action="store_true",
        help="Treat input string as regex")
    args = parser.parse_args()

    helper.initLoger()

    replacename(args.find, args.replace, args.dir if args.dir else os.getcwd(),
                not args.wetrun, args.mode, args.regex)
