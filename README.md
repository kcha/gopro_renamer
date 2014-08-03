GoPro Chaptered Video File Renamer
==================================

This script alters the naming convention of chaptered videos created by GoPro
Hero3 cameras (see
http://gopro.com/support/articles/hero3-and-hero3-file-naming-convention),
which I found be unintuitive. 

For example:
Here are two sets of videos (0892 and 0893) that were broken up into chapters by
the camera and one single video (0891):
 * GOPR0891.mp4
 * GOPR0892.mp4
 * GOPR0893.mp4
 * GP010892.mp4
 * GP010893.mp4
 * GP020893.mp4

I would prefer to see GP010892.mp4 to come after GOPR0892.mp4. For example,
files could be renamed as the following:
 * GOPR0891_1.mp4
 * GOPR0892_1.mp4
 * GOPR0892_2.mp4
 * GOPR0893_1.mp4
 * GOPR0893_2.mp4
 * GOPR0893_3.mp4

Usage
-----

The script was written in Python (2.6+). To run:

~~~~
python gopro_chapter_renamer.py folder_containing_gopro_videos
~~~~

The script will search inside the specified folder for `mp4` files that follow
GoPro's naming convention, and rename them accordingly.

Non-chaptered videos will be renamed as well.

Renaming cannot be undone!

Options
-------

For additional options, run:

~~~~
python gopro_chapter_renamer.py -h
~~~~

To change the starting number (default is 1), use the option `-s`.

To change the filename prefix (default is GOPR), use the option `-p`.

To perform a dry run, use the option `-t`.
