[![Build Status](https://travis-ci.org/kcha/gopro_renamer.svg?branch=master)](https://travis-ci.org/kcha/gopro_renamer)

# GoPro Chaptered Video File Renamer

This script alters the naming convention of chaptered videos created by GoPro
Hero3+ cameras (see
https://gopro.com/help/articles/question_answer/GoPro-Camera-File-Naming-Convention),
which I found to be unintuitive. 

For example:
Here are two sets of videos (0892 and 0893) that were broken up into chapters by
the camera and one single video (0891):
~~~~
GOPR0891.mp4    <- single video
GOPR0892.mp4    <- multi-video A1
GOPR0893.mp4    <- multi-video B1
GP010892.mp4    <- multi-video A2
GP010893.mp4    <- multi-video B2
GP020893.mp4    <- multi-video B3
~~~~

When sorted, I would prefer to see `GP010892.mp4` to come after `GOPR0892.mp4`. For example,
files could be renamed as the following:
~~~~
GOPR0891.mp4 -> GOPR0891_1.mp4
GOPR0892.mp4 -> GOPR0892_1.mp4
GP010892.mp4 -> GOPR0892_2.mp4
GOPR0893.mp4 -> GOPR0893_1.mp4
GP010893.mp4 -> GOPR0893_2.mp4
GP020893.mp4 -> GOPR0893_3.mp4
~~~~

## Installation

If you want to install it with pip for easy access, run:
~~~~
pip install git+https://github.com/kcha/gopro_renamer#egg=gopro_renamer
~~~~

To install manually, download the repository and run:
~~~~
python setup.py install
~~~~

If you don't want to install the script to your environment,
you can also run it directly:
~~~~
python gopro_renamer.py folder_containing_gopro_videos
~~~~

Usage
-----
To use the script, run:
~~~~
gopro_renamer folder_containing_gopro_videos
~~~~

The script will search inside the specified folder for `mp4` files that follow
GoPro's naming convention, and rename them accordingly.

Non-chaptered videos will be renamed as well.

Renaming cannot be undone! A log of changes will be saved in the file `<gopro_directory>/rename.log`.

Options
-------

For additional options, run:

~~~~
gopro_renamer -h
~~~~

  * To change the starting number (default is 1), use the option `-s`.
  * To change the filename prefix (default is GOPR), use `-p`.
  * To rename files with a different extension (default is MP4), use `-e`.

To perform a dry run, use the option `-t`.

_Thank you to all 
[contributors](https://github.com/kcha/gopro_renamer/pulls?q=is%3Apr+is%3Aclosed) who have helped improve this tool!_
