from readdicom import process
import pydicom
import argparse
import sys
import os

# Parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--directory", required=True,
    help="directory to images")
args = vars(ap.parse_args())
dir_path = args["directory"]

# array that stores that data from all DICOM files in the given directory
data = []

# Cycle through files in directory and pass to read_dicom
for root, dirs, files in os.walk(dir_path, topdown=False):    
    for name in files:
        path = os.path.join(root, name)
        data.append(process(path))
    
    # for name in dirs:
    #     path = os.path.join(root, name)
    #     process(path)

print(data)
