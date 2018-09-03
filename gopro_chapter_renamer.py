#!/usr/bin/env python
#
# Copyright (c) 2014,2018 Kevin Ha
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

from __future__ import print_function
import re
import sys
import os
import argparse
import datetime

__version__ = "0.3.3"

def getoptions():
    usage = "usage: python %prog [options] folder_containing_gopro_videos"
    desc = "Rename GoPro video files. Renaming cannot be undone. Use at" + \
           " your own risk. To perform a test run, use option -t."
    parser = argparse.ArgumentParser(description = desc)
    parser.add_argument('--version', action = 'version', version = __version__)
    parser.add_argument('gopro_dir', nargs=1,
                        help='GoPro video directory')
    parser.add_argument('-s', '--start', type = int, default = 1,
            dest = "startnum", 
            help = "Starting chapter number [%(default)s]")
    parser.add_argument('-p', '--prefix', type = str, default = "GOPR",
            dest = "prefix",
            help = "Prefix of renamed files [%(default)s]")
    parser.add_argument('-t', '--test', action = "store_true", dest = "test",
            default = False,
            help = "Perform dry run for testing (no renaming will take place) [%(default)s]")
    parser.add_argument("-n", type = int, default = 3,
            dest = "size",
            help = "Number of digits for chapter number (e.g. if -n is 2, then chapters will"
            " be 01, 02, etc.) [%(default)s]")
    parser.add_argument("-e", "--ext", type = str, default = 'MP4',
            dest = "ext",
            help = "Extension of files to rename (case insensitive) [%(default)s]")
    args = parser.parse_args()
    
    return args

def rename(dir, old, new, dryrun, fout):
    log = "%s -> %s" % (dir + "/" + old, dir + "/" + new) 
    if not dryrun:
        os.rename(dir + "/" + old, dir + "/" + new)
    if fout is not None:
        fout.write("%s -> %s\n" % (old, new))
    print(log)
    
def resize_chapter(num, size, new_format=False):
    if new_format:
        num -= 1
    return '{0:0{1}d}'.format(num, size)

def has_ext(f, ext):
    return bool(re.search(ext, f, re.I))

def main():
    args = getoptions()

    if args.test:
        print("**DRY RUN**")

    logfile = args.gopro_dir[0] + "/rename.log"
    fout = open(logfile, 'w')
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    fout.write("[%s v%s - %s]\n" % (sys.argv[0], __version__, now))
    count = 0
    for myfile in os.listdir(args.gopro_dir[0]):
        if has_ext(myfile, args.ext):
            
            first = re.match(r"(GOPR|GH01|GX01)(\d{4})\." + args.ext, myfile, re.I)

            if first:
                num = resize_chapter(args.startnum, args.size)
                newfirst = args.prefix + first.group(2) + "_" + num + "." + args.ext

                rename(args.gopro_dir[0], myfile, newfirst, args.test, fout) 
                count += 1
            else:

                chapter = re.match(r"(GP|GH|GX)(\d{2})(\d{4})\." + args.ext, myfile, re.I)
                new_format = myfile[0:2] == 'GH'
                if chapter:
                    num = resize_chapter(args.startnum + int(chapter.group(2)), args.size, new_format)
                    newchapter = args.prefix + chapter.group(3) + "_" + num + \
                                 "." + args.ext

                    rename(args.gopro_dir[0], myfile, newchapter, args.test,
                           fout)
                    count += 1
    fout.close()
    print("Renamed %d files" % count, file=sys.stderr)
    if count > 0:
        print("Change log saved in %s" % logfile, file=sys.stderr)
    else:
        os.remove(logfile)

if __name__ == '__main__':
    main()
