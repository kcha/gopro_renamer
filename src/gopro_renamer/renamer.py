#!/usr/bin/env python
#
# Copyright (c) 2014 Kevin Ha
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import importlib.metadata
from pathlib import Path
import re
import argparse
import logging

PROG = 'gopro-renamer'

logger = logging.getLogger(PROG)

__version__ = importlib.metadata.version("gopro_renamer")


def getoptions():
    usage = "%(prog)s [options] folder_containing_gopro_videos"
    desc = (
        "Rename GoPro video files. Renaming cannot be undone. Use at"
        + " your own risk. To perform a test run, use option -t."
    )
    parser = argparse.ArgumentParser(usage=usage, description=desc)
    parser.add_argument("-v", "--version", action="version", version=__version__)
    parser.add_argument("gopro_dir", nargs=1, type=Path, help="GoPro video directory")
    parser.add_argument(
        "-s",
        "--start",
        type=int,
        default=1,
        dest="startnum",
        help="Starting chapter number [%(default)s]",
    )
    parser.add_argument(
        "-p",
        "--prefix",
        type=str,
        default="GOPR",
        dest="prefix",
        help="Prefix of renamed files [%(default)s]",
    )
    parser.add_argument(
        "-t",
        "--test",
        action="store_true",
        dest="test",
        default=False,
        help="Perform dry run for testing (no renaming will take place) [%(default)s]",
    )
    parser.add_argument(
        "-n",
        type=int,
        default=3,
        dest="size",
        help="Number of leading zeroes for chapter number (e.g. if -n is 2, "
        "then chapters will be 01, 02, etc.) [%(default)s]",
    )
    parser.add_argument(
        "-e",
        "--ext",
        type=str,
        default="MP4",
        dest="ext",
        help="Extension of files to rename (case insensitive) [%(default)s]",
    )
    args = parser.parse_args()

    return args


def rename(old: Path, new: Path, dryrun: bool) -> None:
    """Rename file"""
    msg = f"{old} -> {new}"
    if not dryrun:
        old.rename(new)
    logger.info(msg)


def resize_chapter(num: int, size: int, new_format: bool = False) -> str:
    """Reformat chapter numbering"""
    if new_format:
        num -= 1
    return f'{num:0{size}d}'


def has_ext(file: Path, ext: str) -> bool:
    """Check if file contains extension"""
    if not ext.startswith('.'):
        ext = f'.{ext}'
    return ext.upper() == file.suffix.upper()


def main():
    args = getoptions()

    logfile = args.gopro_dir[0] / "gopro-renamer.log"

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[logging.FileHandler(logfile), logging.StreamHandler()],
    )

    logger.info("gopro-renamer v%s", __version__)
    logger.info("Command: %s", args)

    if args.test:
        logger.info("**DRY RUN**")

    count = 0
    for myfile in args.gopro_dir[0].iterdir():
        if has_ext(myfile, args.ext):

            first = re.match(r"(GOPR|GH01|GX01)(\d{4})\." + args.ext, myfile.name, re.I)

            if first:
                num = resize_chapter(args.startnum, args.size)
                newfirst = (
                    args.gopro_dir[0]
                    / f"{args.prefix}{first.group(2)}_{num}.{args.ext}"
                )

                rename(myfile, newfirst, args.test)
                count += 1
            else:
                chapter = re.match(
                    r"(GP|GH|GX)(\d{2})(\d{4})\." + args.ext, myfile.name, re.I
                )
                new_format = myfile.stem[0:2] == "GH"
                if chapter:
                    num = resize_chapter(
                        args.startnum + int(chapter.group(2)), args.size, new_format
                    )
                    newchapter = (
                        args.gopro_dir[0]
                        / f"{args.prefix}{chapter.group(3)}_{num}.{args.ext}"
                    )

                    rename(myfile, newchapter, args.test)
                    count += 1
        else:
            logger.info('Skipping %s', myfile)

    logger.info("Renamed %d files", count)
    logger.info("Change log saved in %s", logfile)


if __name__ == "__main__":
    main()
