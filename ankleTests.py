def testThickness(thickness):
    if thickness < 1.25 or thickness > 2.5:
        return (1, "thickness off")
    return (0, '')

def runTests(ankleData):
    sliceLocations = []
    testResults = {
        'fileTested' : "Ankle Tests",
        'tests' : []
    }
    
    for scan in ankleData:
        dcm_data = scan['data']

        passVal, msg = testThickness(dcm_data["slice_thickness"])
        testResults['tests'].append({
            'file' : scan['filename'],
            'testType' : 'Slice Thickness',
            'criteria' : passVal,
            'passMessage' : msg
        })
        
        sliceLocations.append(dcm_data['slice_location'])
    
    sliceLocations.sort()
    continuousSlices = True
    pastSliceDist = 'x'
    
    for i in range(1, len(sliceLocations)):
        sliceDist = sliceLocations[i] - sliceLocations[i - 1]
        if pastSliceDist != 'x':
            if sliceDist != pastSliceDist:
                continuousSlices = False
                break
        pastSliceDist = sliceDist
    
    if not continuousSlices:
        testResults['tests'].append({
            'file' : 'N/A',
            'testType' : 'Continuous Slices',
            'criteria' : 1,
            'passMessage' : "Slices are not continuous"
        })
    else:
        testResults['tests'].append({
            'file' : 'N/A',
            'testType' : 'Continuous Slices',
            'criteria' : 0,
            'passMessage' : "Slices are continuous"
        })
    
    return [testResults]