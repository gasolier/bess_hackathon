import pydicom
import numpy as np
import os

def read_dicom (file_path):
    dataset  = pydicom.dcmread(file_path)

    # for now just return the pixel data and spacing in a dictionary
    return {
        "pixel_array" : dataset.PixelArray,
        "pixel_spacing" : dataset.PixelSpacing
    }

def read_from_directory (dir_path):
    print(dir_path)
    dicom_arr = []
    for root, dirs, files in os.walk(dir_path):
        print(root, files)
        for f in files:
            print(root + f)
            dicom_arr.append(read_dicom(root + f))
    return dicom_arr