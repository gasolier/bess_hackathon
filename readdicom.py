import pydicom

def process (file_path):
    dataset  = pydicom.dcmread(file_path)

    # print(dataset.elements)

    # for now just return the pixel data and spacing in a dictionary
    return {
        "slice_thickness" : dataset.SliceThickness,
        "slice_location" : dataset.SliceLocation,
        "pixel_array" : dataset.PixelData,
        "pixel_spacing" : dataset.PixelSpacing
    }
