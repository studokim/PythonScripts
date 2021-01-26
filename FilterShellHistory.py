#!/usr/bin/python3
# -*- coding: utf-8 -*-

#  Takes text .zsh_history file and converts it to a sorted list of unique commands
#
#  Shell arguments: input_file output_file

import sys
hist = open(str(sys.argv[1]))
try:
    outname = str(sys.argv[2])
except:
    outname = "res.txt"

temp = ""
lines = []
for line in hist:
    line = line.strip()
    try:
        #  Ensure that the command is not empty and not mistaken like "\" or "cd ~\"
        if (line) and (not (line[-1] == '\\' and (len(line) == 1 or line[-2] != '\\'))):
            temp += line.rstrip(r"\\").replace("sudo ", "")
            if (line[-2:] != r"\\"):
                lines.append(' '.join(temp[15:].split()))
                temp = ""
    except:
        print("Error on the line:\n>>>" + line)
        break
hist.close()

lines = sorted(list(set(lines)))

outp = open(outname, "w")
for line in lines:
    outp.write(line + '\n')
outp.close()
