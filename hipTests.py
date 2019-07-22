def runTests(dcm_data):
    # # Pass/Fail if criteria = 0; pass, else if criteria = 1 then incorrect slice thickness
    # criteria = 0 
    # ss = dataset.SliceThickness
    # if ss < 1.25 and ss > 2:
    #     criteria = 1
    result = 0
    ss = dcm_data["slice_thickness"]
    
    if ss < 1.25 and ss > 2:
        result = 1

    return result