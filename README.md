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
irrevocably renamed.

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
gopro-renamer -h
~~~~

  * To change the starting number (default is 1), use the option `-s`.
  * To change the filename prefix (default is GOPR), use `-p`.
  * To rename files with a different extension (default is MP4), use `-e`.

To perform a dry run, use the option `-t`.

## Disclaimer

This is a personal project and not affiliated with GoPro. Use at your own risk
(see `LICENSE`).

## Acknowledgements

_Thank you to all
[contributors](https://github.com/kcha/gopro_renamer/graphs/contributors)
who have helped improve this tool!_

