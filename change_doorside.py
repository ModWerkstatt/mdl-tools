#!/usr/bin/env python3
# v.0.0.1

# import the needed requirements
import re
import sys
import os
from shutil import copyfile

# name of input and output files
if len(sys.argv)==1:
    print('No file specified. Exiting. Please use the script like python3 doors.py yourfile.mdl')
    sys.exit()
# we have an input file, start processing it
ifilename = sys.argv[1]
ofilename = ifilename+'.MODIFIED'
ifile = open(ifilename)
ofile = open(ofilename,'w')
# make a backup file just to be sure
backup_name = 'backup_REMOVE_ME_BEFORE_UPLOAD'
os.makedirs(backup_name,exist_ok=True)
copyfile(ifilename, backup_name + '/' + ifilename)
# initialize variables
lod = -1
counter = 0
max_counter = []
pop_counter = 0
# compile regex pattern
left_pattern = re.compile("doors_left")
right_pattern = re.compile("doors_right")
# now we can read every line of file and see if we can or should process it
for line in ifile:
    # node - we have a node found, set counter for meshes
    if left_pattern.search(line):
        line = left_pattern.sub("doors_right",line)
    # replace "_lod$" with actual lod number
    elif right_pattern.search(line):
        line = right_pattern.sub("doors_left",line)
    ofile.write(line)
# replace original file with modified file
os.remove(ifilename)
os.rename(ofilename, ifilename)
# print some details about the work done
print("alles erledigt!")
