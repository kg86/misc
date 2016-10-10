#!/usr/bin/env python3

'''
print lines which have non ascii characters.
'''

import sys
from optparse import OptionParser

usage = 'usage: %prog [options]'

if __name__=='__main__':
  parser = OptionParser()
  parser.set_usage(usage)
  parser.add_option('-n', '--line-number', dest='line_number', help='Each output line is preceded by its reltive line number in the file', action='store_true')
  (opt, args) = parser.parse_args()
  if len(args) == 0:
    fs = [('', sys.stdin)]
  else:
    fs = ((fname, open(fname, 'r')) for fname in args)
  for fname, fobj in fs:
    pre = (fname + ':') if fname else ''
    for linei, line in enumerate(fobj):
      if any(ord(c) > 255 for c in line):
        if opt.line_number:
          sys.stdout.write (pre + str(linei) + ':' + line)
        else:
          sys.stdout.write (pre + line)
