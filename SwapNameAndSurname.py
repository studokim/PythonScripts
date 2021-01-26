#!/usr/bin/python3
# -*- coding: utf-8 -*-

#  Takes text file where Name and Surname are separated
#  with ' ' or anything (look separator argument)
#  and writes them vice versa
#
#  Shell arguments: input_file output_file separator
#
#  .rstrip() method strips all kinds of newlines
#  and trailing whitespaces

import sys
inp = open(str(sys.argv[1]))
outp = open(str(sys.argv[2]), "w")
try:
    separator = str(sys.argv[3])
except:
    separator = ' '

for line in inp:
    pair = line.rstrip().split(' ')
    outp.write(str(pair[1] + separator + pair[0] + '\n'))
inp.close()
outp.close()
