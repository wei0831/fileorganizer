#!/usr/bin/python
""" replacename.py

"""
import os
import os.path
import re
import logging
import click
from fileorganizer import _helper
from fileorganizer._helper import find_matches_exclude
from fileorganizer._transaction import Transaction

__author__ = "Jack Chang <wei0831@gmail.com>"

DESCRIPTION = "Find string in File name/Folder name and replace with another string"


def _replacename(find, replace, work_dir, mode=0, exclude=None):
    regex_find = re.compile(find)
    matches = find_matches_exclude(mode, find, work_dir, exclude)
    get_newname = lambda f: regex_find.sub(replace, f)

    for oldname in matches:
        newname = get_newname(oldname)

        if not newname == oldname and not newname == "":
            oldnamepath = os.path.join(work_dir, oldname)
            newnamepath = os.path.join(work_dir, newname)

            yield Transaction(oldnamepath, newnamepath, "mv")


@click.command()
@click.argument('find', type=click.STRING)
@click.argument('replace', type=click.STRING)
@click.argument('work_dir', type=click.Path(exists=True, resolve_path=True))
@click.option(
    '--exclude',
    '-e',
    default=None,
    type=click.STRING,
    help="Exclude regex pattern")
@click.option(
    '--mode',
    '-m',
    default=0,
    type=click.INT,
    help="0: FILE_ONLY, 1: FOLDER_ONLY, 2: BOTH")
@click.option('--wetrun', '-w', is_flag=True, help="Commit changes")
def replacename(find, replace, work_dir, exclude=None, mode=0, wetrun=False):
    """ Find string in File name/Folder name and replace with another string

    \b
    Args:
        find (str): Regex string to find in filename/foldername
        replace (str): Regex string to replace in filename/foldername
        work_dir (str): Working Directory
        exclude (str, optional): Regex string to exclude in mattches
        mode (int, optional): 0=FILE ONLY, 1=FOLDER ONLY, 2=BOTH
        wetrun (bool, optional): Test Run or not
    """
    _helper.init_loger()
    this_name = os.path.basename(__file__)
    loger = logging.getLogger(this_name)
    loger.info("Replace \"%s\" with \"%s\" in \"%s\"; Mode %s", find, replace,
               work_dir, mode)
    loger.info("=== %s [%s RUN] start ===", this_name, "WET"
               if wetrun else "DRY")

    for item in _replacename(find, replace, work_dir, mode, exclude):
        if wetrun:
            item.commit()
        else:
            loger.info("%s", item)

    loger.info("=== %s end ===", this_name)


if __name__ == "__main__":
    replacename()
