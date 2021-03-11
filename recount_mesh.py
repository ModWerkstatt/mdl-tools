#!/usr/bin/env python3
# v.0.0.5

# import the needed requirements
import re
import sys
import os
from shutil import copyfile

# name of input and output files
if len(sys.argv)==1:
    print('No file specified. Exiting. Please use the script like python3 count.py yourfile.mdl')
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
node_pattern = re.compile("node[\s]=[\s]")
lod_pattern = re.compile("_lod\$")
pattern = re.compile("\d+")
# now we can read every line of file and see if we can or should process it
for line in ifile:
    # node - we have a node found, set counter for meshes
    if node_pattern.search(line):
        max_counter.append(counter-1)
        counter = 0
        lod += 1
    # children - a children adds 1 to the counter of meshes
    # counter<15 is a workaround for UIC-X, don't use children if we are behind the bogies
    elif "children" in line: # and counter<15:
        counter += 1
    # mesh - a mesh entry, we need to do the main things here
    elif "_meshId" in line:
        line = pattern.sub(str(counter),line) # replace the current _meshId with the current one
        counter += 1
    # replace "_lod$" with actual lod number
    elif lod_pattern.search(line):
        line = lod_pattern.sub("_lod"+str(lod),line)
    # we have reached the metadata and close some things
    #elif "configs" in line:
    #    max_counter.append(counter-1)
     #   max_counter.pop(0)
    # just for UIC-X, for everything else we have more entries
     #elif "backForwardParts" in line:
     #   act = max_counter[pop_counter]
     #   line = pattern.sub(str(act),line)
     #   pop_counter += 1
    ofile.write(line)
# replace original file with modified file
os.remove(ifilename)
os.rename(ofilename, ifilename)
# print some details about the work done
print("gefunden bis: LOD"+str(lod))
max_counter.append(counter-1)
lod = -1
for val in max_counter:
    if (val >= 0):
        print("Max Counter LOD"+str(lod)+":"+str(val))
    lod+=1
print("-------------------")
print("alles erledigt!")
