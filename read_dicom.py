import pydicom
import numpy as np

def read_dicom (file_path):
    dataset  = pydicom.dcmread(file_path)

    # for now just return the pixel data and spacing in a dictionary
    return {
        "pixel_array" : dataset.PixelArray,
        "pixel_spacing" : dataset.PixelSpacing
    }

