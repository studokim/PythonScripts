#!/usr/bin/python3
# -*- coding: utf-8 -*-

#  Takes text file where terms and defs are separated
#  with '-'or '--' or '–' or anything (look separator argument)
#  and converts it to .csv, which may be imported to Kahoot
#
#  Shell arguments: input_file output_file separator answer_quantity time_limit

import sys
inp = open(str(sys.argv[1]))
separator = str(sys.argv[3])
answer_quantity = int(sys.argv[4])
time_limit = int(sys.argv[5])

terms = []
defs = []
for line in inp:
    pair = line.rstrip().split(separator)
    terms.append(pair[0])
    defs.append(pair[1])
inp.close()

from random import randint
import csv
outp = open(str(sys.argv[2]), "w", newline='')
length = len(terms)
for i in range(length):
    correct = randint(1, answer_quantity)
    ans = [None for i in range(5)]
    ans[0] = terms[i]
    ans[correct] = defs[i]
    for j in range(1, answer_quantity + 1):
        if (j != correct):
            k = randint(0, length - 1)
            while (defs[k] in ans[1:4]):
                k = randint(0, length - 1)
            ans[j] = defs[k]
    ans.append(time_limit)
    ans.append(correct)
    csv.writer(outp).writerow(ans)
outp.close()
