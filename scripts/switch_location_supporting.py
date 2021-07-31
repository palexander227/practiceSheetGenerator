import glob
import os

"""

In the questions, switch the location of the 'Supporting' folder that contains 
supporting images or tables. This needs to reflect the (relative) location where 
the final compilation will occur.

"""


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

files_dir = os.path.join('..','questions')

# Find all problem files
files = glob.glob(os.path.join(files_dir,'*tex'))
# Loop through problems
for file in files:
    # read problem
    with open(file,'r') as f:
        lines = f.readlines()
    outfile = open(file,'w')
    # Loop through lines
    for line in lines:
        if '../../Supporting/' in line:
            line = line.replace('../../Supporting/','support/')
        else:
            pass
        outfile.write(line)
    outfile.close()





