GoPro Chaptered Video File Renamer
==================================

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
Usage
-----

The script was written in Python (2.7+ and 3.3+). To run:

~~~~
python gopro_chapter_renamer.py folder_containing_gopro_videos
~~~~

The script will search inside the specified folder for `mp4` files that follow
GoPro's naming convention, and rename them accordingly.

Non-chaptered videos will be renamed as well.

Renaming cannot be undone! A log of changes will be saved in the file `<gopro_directory>/rename.log`.

Options
-------

For additional options, run:

~~~~
python gopro_chapter_renamer.py -h
~~~~

  * To change the starting number (default is 1), use the option `-s`.
  * To change the filename prefix (default is GOPR), use `-p`.
  * To rename files with a different extension (default is MP4), use `-e`.

To perform a dry run, use the option `-t`.
