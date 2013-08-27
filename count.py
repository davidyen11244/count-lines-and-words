#!/usr/bin/python

import os
import commands
import re
import sys


def main(args):
    if len(args) != 1:
        print 'Usage: python line_number.py <path_to_directory>'

    line = 0
    word = 0

    for root, dirs, files in os.walk(args[0]):
        for f in files:
            output = commands.getoutput('wc %s/%s' % (root, f))
            match = re.search('\s+(\d+)\s+(\d+).*', output)
            if match:
                line += int(match.group(1))
                word += int(match.group(2))

    print 'You wrote %d lines and %d words!!' % (line, word)


if __name__ == '__main__':
    main(sys.argv[1:])
