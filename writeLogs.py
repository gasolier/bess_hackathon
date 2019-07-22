def write_logs(test_results):
    # Write to a logs.txt file
    f = open("logs.txt", "a+")

    for result in test_results:
        criteria = result["criteria"]
        testType = result["testType"]
        fileTested = result["fileTested"]
        passMessage = result["passMessage"]
        
        f.write(f"Filename: {fileTested}\n")
        f.write(f"Test: {testType}\n")
        
        if criteria == 0:
            f.write("Criteria: Passed") 
        elif criteria == 1:
            f.write(f"Criteria: Failed: error: {passMessage}")
        
        f.write('\n')