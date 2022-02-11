[![Build Status](https://travis-ci.org/kcha/gopro_renamer.svg?branch=master)](https://travis-ci.org/kcha/gopro_renamer)

# GoPro Chaptered Video File Renamer

This script alters the naming convention of chaptered videos created by GoPro
HERO3+ cameras (see
https://gopro.com/help/articles/question_answer/GoPro-Camera-File-Naming-Convention)
into a more user-friendly format.


To illustrate this, take for example two sets of videos (0892 and 0893) that
were broken up into chapters by
the camera and one single video (0891):

~~~~
GOPR0891.mp4    <- single video
GOPR0892.mp4    <- multi-video A1
GOPR0893.mp4    <- multi-video B1
GP010892.mp4    <- multi-video A2
GP010893.mp4    <- multi-video B2
GP020893.mp4    <- multi-video B3
~~~~

When sorted, the chaptered videos are not naturally ordered together as one
would expect. `gopro_renamer` addresses this by renaming your files into
something like this:

~~~~
GOPR0891.mp4 -> GOPR0891_1.mp4
GOPR0892.mp4 -> GOPR0892_1.mp4
GP010892.mp4 -> GOPR0892_2.mp4
GOPR0893.mp4 -> GOPR0893_1.mp4
GP010893.mp4 -> GOPR0893_2.mp4
GP020893.mp4 -> GOPR0893_3.mp4
~~~~

## Installation

The recommended installation method is via `pip`:

~~~~
pip install gopro_renamer
~~~~

To install manually, clone this repository and run:
~~~~
pip install .
~~~~


## Usage

If desired, make a backup of your files before proceeding as your files will be
irrevocably renamed.

To run the app:

~~~~
gopro-renamer <gopro_directory>
~~~~

The script will search inside the specified folder for `mp4` files that follow
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

This is a personal project and has no affiliation with GoPro. Use at
your own risk (see `LICENSE`).

## Acknowledgements

_Thank you to all
[contributors](https://github.com/kcha/gopro_renamer/graphs/contributors)
who have helped improve this tool!_

