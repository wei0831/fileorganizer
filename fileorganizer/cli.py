#!/usr/bin/python
""" cli.py
    Click Wrappers
"""
import click
from fileorganizer.folderin import folderin
from fileorganizer.folderout import folderout
from fileorganizer.moveintofolder import moveintofolder
from fileorganizer.fanhaorename import fanhaorename
from fileorganizer.replacename import replacename
from fileorganizer.renameafterfolder import renameafterfolder
from fileorganizer.fanhaofolderin import fanhaofolderin

__author__ = "Jack Chang <wei0831@gmail.com>"


@click.command()
@click.argument('work_dir', type=click.Path(exists=True, resolve_path=True))
@click.option('--wetrun', '-w', is_flag=True, help="Commit changes")
def cli_folderin(work_dir, wetrun=False):
    """ Click Wrapper: Put files into folder with the same name

    \b
    Args:
      work_dir (str): Working Directory
      wetrun (bool, optional): Test Run or not
    """
    folderin(work_dir, wetrun)

@click.command()
@click.argument('work_dir', type=click.Path(exists=True, resolve_path=True))
@click.option('--wetrun', '-w', is_flag=True, help="Commit changes")
def cli_fanhaofolderin(work_dir, wetrun=False):
    """ Click Wrapper: Organize file XXX-YYY into folder XXX

    \b
    Args:
      work_dir (str): Working Directory
      wetrun (bool, optional): Test Run or not
    """
    fanhaofolderin(work_dir, wetrun)

@click.command()
@click.argument('work_dir', type=click.Path(exists=True, resolve_path=True))
@click.option(
    '--to_dir',
    '-t',
    default=None,
    type=click.Path(exists=True, resolve_path=True),
    help="Target Directory")
@click.option('--wetrun', '-w', is_flag=True, help="Commit changes")
def cli_folderout(work_dir, to_dir=None, wetrun=False):
    """ Click Wrapper: Move files out of folders
    
    \b
    Args:
        work_dir (str): Working Directory
        to_dir (str, optional): Target Directory
        wetrun (bool, optional): Test Run or not
    """
    folderout(work_dir, to_dir, wetrun)


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
@click.option('--insensitive', '-i', is_flag=True, help="Case Insensitive")
@click.option('--wetrun', '-w', is_flag=True, help="Commit changes")
def cli_moveintofolder(find,
                       work_dir,
                       to_dir,
                       exclude=None,
                       mode=0,
                       insensitive=False,
                       wetrun=False):
    """ Click Wrapper: Move matching files/folder into a folder

    \b
    Args:
        find (str): Regex string to find in filename/foldername
        work_dir (str): Working Directory
        to_dir (str): Target Directory
        exclude (str, optional): Regex string to exclude in mattches
        mode (int, optional): 0=FILE ONLY, 1=FOLDER ONLY, 2=BOTH
        wetrun (bool, optional): Test Run or not
    """
    moveintofolder(find, work_dir, to_dir, exclude, mode, not insensitive,
                   wetrun)


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
def cli_replacename(find,
                    replace,
                    work_dir,
                    exclude=None,
                    mode=0,
                    wetrun=False):
    """ Click Wrapper: Find string in File name/Folder name and replace with another string

    \b
    Args:
        find (str): Regex string to find in filename/foldername
        replace (str): Regex string to replace in filename/foldername
        work_dir (str): Working Directory
        exclude (str, optional): Regex string to exclude in mattches
        mode (int, optional): 0=FILE ONLY, 1=FOLDER ONLY, 2=BOTH
        wetrun (bool, optional): Test Run or not
        this_name (str, optional): caller name
    """
    replacename(find, replace, work_dir, exclude, mode, wetrun)


@click.command()
@click.argument('work_dir', type=click.Path(exists=True, resolve_path=True))
@click.argument('tag', type=click.STRING)
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
def cli_fanhaorename(work_dir, tag, exclude=None, mode=0, wetrun=False):
    """ Click Wrapper: Batch Rename Fanhao

    \b
    Args:
        work_dir (str): Working Directory
        tag (str): Fanhao tag
        exclude (str, optional): Regex string to exclude in mattches
        mode (int, optional): 0=FILE ONLY, 1=FOLDER ONLY, 2=BOTH
        wetrun (bool, optional): Test Run or not
    """
    fanhaorename(work_dir, tag, exclude, mode, wetrun)


@click.command()
@click.argument('find', type=click.STRING)
@click.argument('work_dir', type=click.Path(exists=True, resolve_path=True))
@click.option(
    '--exclude',
    '-e',
    default=None,
    type=click.STRING,
    help="Exclude regex pattern")
@click.option('--wetrun', '-w', is_flag=True, help="Commit changes")
def cli_renameafterfolder(find, work_dir, exclude=None, wetrun=False):
    """ Click Wrapper: Rename all files inside folder with folder name

    \b
    Args:
        find (str): Regex string to find in filename/foldername
        work_dir (str): Working Directory
        exclude (str, optional): Regex string to exclude in mattches
        wetrun (bool, optional): Test Run or not
    """
    renameafterfolder(find, work_dir, exclude, wetrun)
