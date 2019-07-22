import pydicom

def process (file_path):
    dataset  = pydicom.dcmread(file_path)

    # for now just return the pixel data and spacing in a dictionary
    return {
        "filename" : file_path,
        "body_part" : dataset.BodyPartExamined,
        "slice_thickness" : dataset.SliceThickness,
        "slice_location" : dataset.SliceLocation,
        #"pixel_array" : dataset.PixelArray,
        "pixel_spacing" : dataset.PixelSpacing
    }
