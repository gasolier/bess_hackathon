from readdicom import process
import hipTests, kneeTests, ankleTests
import writeLogs
import pydicom
import argparse
import os


# Parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--directory", required=True,
    help="directory to images")
args = vars(ap.parse_args())
dir_path = args["directory"]

# array that stores that data from all DICOM files in the given directory
patientData = {
    "hipScans" : [],
    "kneeScans" : [],
    "ankleScans" : []
}

# go through the sub-directories and read the data in these into our
# patientData variable
for root, dirs, _ in os.walk(dir_path, topdown=False):    
    for d in dirs:
        next_down = os.path.join(dir_path, d)
        for _, _, files in os.walk(next_down):
            for f in files:
                # check our folder type
                if d == "Knee":
                    patientData["kneeScans"].append({'filename' : f, 'data' : process(os.path.join(next_down, f))})
                elif d == "Hip":
                    patientData["hipScans"].append({'filename' : f, 'data' : process(os.path.join(next_down, f))})
                elif d == "Ankle":
                    patientData["ankleScans"].append({'filename' : f, 'data' : process(os.path.join(next_down, f))})

all_tests = []

# run the test
for scanType in patientData.keys():
    if scanType == "hipScans":
        all_tests += hipTests.runTests(patientData[scanType])
    elif scanType == "kneeScans":
        all_tests += kneeTests.runTests(patientData[scanType])
    elif scanType == "ankleScans":
        all_tests += ankleTests.runTests(patientData[scanType])

# write to the log file
writeLogs.write_logs(all_tests)