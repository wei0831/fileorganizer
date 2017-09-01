#!/usr/bin/python
""" folderout.py

"""
import os
import logging
import click
from fileorganizer import _helper
from fileorganizer._transaction import Transaction
from fileorganizer._helper import find_matches_exclude

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
            yield Transaction(old_path, new_path, "mv")

    for folder in dir_towork:
        yield Transaction(folder, None, "rmdir")


@click.command()
@click.argument('work_dir', type=click.Path(exists=True, resolve_path=True))
@click.option(
    '--to_dir',
    '-t',
    default=None,
    type=click.Path(exists=True, resolve_path=True),
    help="Target Directory")
@click.option('--wetrun', '-w', is_flag=True, help="Commit changes")
def folderout(work_dir, to_dir=None, wetrun=False):
    """ Move files out of folders
    
    \b
    Args:
        work_dir (str): Working Directory
        to_dir (str, optional): Target Directory
        wetrun (bool, optional): Test Run or not
    """
    if to_dir is None:
        to_dir = work_dir

    _helper.init_loger()
    this_name = os.path.basename(__file__)
    loger = logging.getLogger(this_name)
    loger.info("Move files in folders in \"%s\" to \"%s\"", work_dir, to_dir)
    loger.info("=== %s [%s RUN] start ===", this_name, "WET"
               if wetrun else "DRY")

    for item in _folderout(work_dir, to_dir):
        if wetrun:
            item.commit()
        else:
            loger.info("%s", item)

    loger.info("=== %s End ===", this_name)


if __name__ == "__main__":
    folderout()
