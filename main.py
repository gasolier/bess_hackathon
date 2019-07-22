from readdicom import process
import pydicom
import argparse
import os

# Parse the arguments
print("success")
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--directory", required=True,
    help="directory to images")
args = vars(ap.parse_args())
dir_path = args["directory"]

# Cycle through files in directory and pass to read_dicom
for root, dirs, files in os.walk(dir_path, topdown=False):
    for name in files:
        path = os.path.join(root, name)
        process(path)
    for name in dirs:
        path = os.path.join(root, name)
        process(path)

