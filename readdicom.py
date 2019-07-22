import pydicom
import numpy as np
import sys
import os

def process (file_path):
    dataset  = pydicom.dcmread(file_path)

    # Pass/Fail if criteria = 0; pass, else if criteria = 1 then incorrect slice thickness
    criteria = 0 
    ss = dataset.SliceThickness
    if ss < 1.25 and ss > 2:
        criteria = 1 

    # Write to a logs.txt file
    f = open("logs.txt", "a+")  
    f.write("Filename: {}".format(file_path))
    f.write('\n')  
    f.write("Body Part: {}".format(dataset.BodyPartExamined))
    f.write('\n')  
    if criteria == 0:
        f.write("Criteria: Passed, slice thickness {}".format(dataset.SliceThickness)) 
    elif criteria == 1:
        f.write("Criteria: Failed, slice thickness outside of 1.25-2mm, actual value {}".format(dataset.SliceThickness))
    f.write('\n')

    # for now just return the pixel data and spacing in a dictionary
    return {
        "filename" : file_path,
        "pass/fail" : criteria,
        "body_part" : dataset.BodyPartExamined,
        "slice_thickness" : dataset.SliceThickness,
        "slice_location" : dataset.SliceLocation,
        #"pixel_array" : dataset.PixelArray,
        "pixel_spacing" : dataset.PixelSpacing
    }
