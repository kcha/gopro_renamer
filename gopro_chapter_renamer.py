#!/usr/bin/env python

import re
import sys
import os
from optparse import OptionParser

def getoptions():
    usage = "usage: python %prog [options] folder_containing_gopro_videos"
    desc = "Rename GoPro video files"
    parser = OptionParser(usage = usage, description = desc)
    parser.add_option('-s', '--start', type = "int", default = 1,
            dest = "startnum", 
            help = "Starting chapter number [%default]")
    parser.add_option('-p', '--prefix', type = "string", default = "GOPR",
            dest = "prefix",
            help = "Filename prefix [%default]")
    parser.add_option('-t', '--test', action = "store_true", dest = "test",
            default = False,
            help = "Perform dry run for testing (no renaming will take place) [%default]")
    parser.add_option("-n", type = "int", default = 3,
            dest = "size",
            help = "Number of digits for chapter number (e.g. if -n is 2, then chapters will"
            " be 01, 02, etc.) [%default]")
    (opts, args) = parser.parse_args()
    
    if len(args) < 1: 
        print >> sys.stderr, "Error: missing input folder\n"
        parser.print_help()
        exit(-1)
 
    return (opts, args)

def rename(dir, old, new):
    if opts.test:
        print "%s -> %s" % (dir + "/" + old, dir + "/" + new)
    else:
        os.rename(dir + "/" + old, dir + "/" + new)
    
def resize_chapter(num):
    return '{0:0{1}d}'.format(num, opts.size)

def main():

    if opts.test:
        print "DRY RUN"

    count = 0
    for myfile in os.listdir(args[0]):
        if myfile.endswith(".mp4"):
            
            first = re.match(r"GOPR(\d{4})\.mp4", myfile)

            if first:
                num = resize_chapter(opts.startnum)
                newfirst = opts.prefix + first.group(1) + "_" + num + ".mp4"

                rename(args[0], myfile, newfirst) 
                count += 1
            else:

                chapter = re.match(r"GP(\d{2})(\d{4})\.mp4", myfile)
                if chapter:
                    num = resize_chapter(opts.startnum + int(chapter.group(1)))
                    newchapter = opts.prefix + chapter.group(2) + "_" + num + ".mp4"

                    rename(args[0], myfile, newchapter)
                    count += 1

    print >> sys.stderr, "Renamed %d files" % count

if __name__ == '__main__':
    (opts, args) = getoptions()
    main()
