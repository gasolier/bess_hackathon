def testThickness(thickness):
    if thickness < 1.25 and thickness > 2.5:
        return (1, "thickness off")
    return (0, '')

def runTests(file_name, dcm_data):
    testResults = {
        'fileTested' : file_name,
        'tests' : []
    }

    passVal, msg = testThickness(dcm_data["slice_thickness"])
    testResults['tests'].append({
        'testType' : 'Slice Thickness',
        'criteria' : passVal,
        'passMessage' : msg
    })

    return testResults