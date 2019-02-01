#!/usr/bin/python
"""
################################################################################
join all part files in a dir created by split.py, to re-create file.
This is roughly like a 'cat fromdir/* > tofile' command on unix, but is
more portable and configurable, and exports the join operation as a
reusable function. Relies on sort order of filenames: must be same
length. Could extend split/join to pop up Tkinter file selectors.
################################################################################
"""

import os
import sys

readsize = 1024


def join(fromdir, tofile):
    output = open(tofile, 'wb')
    files = os.listdir(fromdir)
    for filename in files:
        fileobj = open(os.path.join(fromdir, filename), 'rb')
        while True:
            filebytes = fileobj.read(readsize)
            if not filebytes:
                break
            output.write(filebytes)
        fileobj.close()
    output.close()


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[3] == '-help':
        print('join files [fromdir tofile]')
    else:
        if len(sys.argv) != 3:
            interactive = True
            fromdir = input('Directory containing part files? ')
            tofile = input('Name of file to be recreated? ')
        else:
            interactive = False
            fromdir, tofile = sys.argv[1:]
            absfrom, absto = map(os.path.abspath, [fromdir, tofile])
            print('Joining', absfrom, 'to make', absto)
            try:
                join(fromdir, tofile)
            except:
                print('Error joining files:')
                print(sys.exc_info()[0], sys.exc_info()[1])
            else:
                print('Join complete: see', absto)
            if interactive:
                input('Press Enter key')  # pause if clicked
