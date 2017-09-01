#!/usr/bin/python
""" moveintofolder.py

"""
import os
import logging
import click
from fileorganizer import _helper
from fileorganizer._transaction import Transaction
from fileorganizer._helper import find_matches_exclude

__author__ = "Jack Chang <wei0831@gmail.com>"

DESCRIPTION = "Move matching files/folder into a folder"


def _moveintofolder(find, work_dir, to_dir, exclude=None, mode=0):
    matches = find_matches_exclude(mode, find, work_dir, exclude)

    for item in matches:
        oldnamepath = os.path.join(work_dir, item)
        newnamepath = os.path.join(to_dir, item)

        yield Transaction(oldnamepath, newnamepath, "mv")


@click.command()
@click.argument('find', type=click.STRING)
@click.argument('work_dir', type=click.Path(exists=True, resolve_path=True))
@click.argument('to_dir', type=click.Path(resolve_path=True, dir_okay=True))
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
def moveintofolder(find, work_dir, to_dir, exclude=None, mode=0, wetrun=False):
    """ Move matching files/folder into a folder

    \b
    Args:
        find (str): Regex string to find in filename/foldername
        work_dir (str): Working Directory
        to_dir (str): Target Directory
        exclude (str, optional): Regex string to exclude in mattches
        mode (int, optional): 0=FILE ONLY, 1=FOLDER ONLY, 2=BOTH
        wetrun (bool, optional): Test Run or not
    """
    _helper.init_loger()
    this_name = os.path.basename(__file__)
    loger = logging.getLogger(this_name)
    loger.info(
        "Matches \"%s\" in \"%s\"; Excludes \"%s\"; Moved to \"%s\"; Mode %s",
        find, work_dir, exclude, to_dir, mode)
    loger.info("=== %s [%s RUN] start ===", this_name, "WET"
               if wetrun else "DRY")

    for item in _moveintofolder(find, work_dir, to_dir, exclude, mode):
        if wetrun:
            item.commit()
        else:
            loger.info("%s", item)

    loger.info("=== %s End ===", this_name)


if __name__ == "__main__":
    moveintofolder()
