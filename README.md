[![Build Status](https://travis-ci.org/kcha/gopro_renamer.svg?branch=master)](https://travis-ci.org/kcha/gopro_renamer)

# GoPro Chaptered Video File Renamer

This script alters the naming convention of chaptered videos created by older GoPro
HERO3 to HERO 2018 cameras (see
https://gopro.com/help/articles/question_answer/GoPro-Camera-File-Naming-Convention)
into a more user-friendly format.

In these older cameras, chaptered video files are named such that they don't
appear next to each other when ordered. To illustrate this, take for example
two sets of videos (892 and 893) that were broken up into chapters by
the camera and one single video (891):

~~~~
GOPR0891.mp4    <- single video 891
GOPR0892.mp4    <- multi-video 892-1
GOPR0893.mp4    <- multi-video 893-1
GP010892.mp4    <- multi-video 892-2
GP010893.mp4    <- multi-video 893-2
GP020893.mp4    <- multi-video 893-3
~~~~

`gopro_renamer` addresses this by renaming your files so that they are grouped
together when ordered:

~~~~
GOPR0891.mp4 -> GOPR0891_1.mp4
GOPR0892.mp4 -> GOPR0892_1.mp4
GP010892.mp4 -> GOPR0892_2.mp4
GOPR0893.mp4 -> GOPR0893_1.mp4
GP010893.mp4 -> GOPR0893_2.mp4
GP020893.mp4 -> GOPR0893_3.mp4
~~~~

## Installation

Install via `pip`:

~~~~
pip install gopro_renamer
~~~~

To install manually, clone this repository and run:

~~~~
cd gopro_renamer
pip install .
~~~~


## Usage

If desired, make a backup of your files before proceeding as your files will be
irrevocably renamed. You can also perform a dry-run by including the `-t` flag.

To run the app:

~~~~
gopro-renamer <gopro_directory>
~~~~

The app will search inside the specified folder for `mp4` files that follow
GoPro's naming convention, and rename them accordingly.

Non-chaptered videos will be renamed as well.

A log of changes will be saved in the file `<gopro_directory>/gopro-renamer.log`.

## Options

For additional options, run:

~~~~
> gopro-renamer -h

usage: renamer.py [options] folder_containing_gopro_videos

Rename GoPro video files. Renaming cannot be undone. Use at your own risk. To perform a test
run, use option -t.

positional arguments:
  gopro_dir             GoPro video directory

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -s STARTNUM, --start STARTNUM
                        Starting chapter number [1]
  -p PREFIX, --prefix PREFIX
                        Prefix of renamed files [GOPR]
  -t, --test            Perform dry run for testing (no renaming will take place) [False]
  -n SIZE               Number of digits for chapter number (e.g. if -n is 2, then chapters
                        will be 01, 02, etc.) [3]
  -e EXT, --ext EXT     Extension of files to rename (case insensitive) [MP4]
~~~~


## Disclaimer

This is a personal project and not affiliated with GoPro. Use at your own risk
(see `LICENSE`).

## Acknowledgements

_Thank you to all
[contributors](https://github.com/kcha/gopro_renamer/graphs/contributors)
who have helped improve this tool!_

