#!/usr/bin/python
""" folderin.py

"""
import os
import logging
import click
from fileorganizer import _helper
from fileorganizer._transaction import Transaction
from fileorganizer._helper import find_matches_exclude

__author__ = "Jack Chang <wei0831@gmail.com>"

DESCRIPTION = "Put files into folder with the same name"


def _folderin(work_dir):
    matches = find_matches_exclude(0, None, work_dir)

    for files in matches:
        form_dir = os.path.join(work_dir, files)
        to_dir = os.path.join(work_dir, os.path.splitext(files)[0], files)
        yield Transaction(form_dir, to_dir, "mv")


@click.command()
@click.argument('work_dir', type=click.Path(exists=True, resolve_path=True))
@click.option('--wetrun', '-w', is_flag=True, help="Commit changes")
def folderin(work_dir, wetrun=False):
    """ Put files into folder with the same name

    \b
    Args:
      work_dir (str): Working Directory
      wetrun (bool, optional): Test Run or not
    """
    _helper.init_loger()
    this_name = os.path.basename(__file__)
    loger = logging.getLogger(this_name)

    loger.info("Files move to individual folders in \"%s\"", work_dir)
    loger.info("=== %s [%s RUN] start ===", this_name, "WET"
               if wetrun else "DRY")

    for item in _folderin(work_dir):
        if wetrun:
            item.commit()
        else:
            loger.info("%s", item)

    loger.info("=== %s End ===", this_name)


if __name__ == "__main__":
    folderin()
