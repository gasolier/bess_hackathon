def write_logs(test_results):
    # Write to a logs.txt file
    f = open("logs.txt", "a+")

    for result in test_results:
        # print(resultType)
        fileTested = result["fileTested"]
        f.write(f"Filename: {fileTested}\n")

        for test in result['tests']:
            testType = test["testType"]
            criteria = test["criteria"]
            passMessage = test["passMessage"]
            
            f.write(f"  Test: {testType} - {'passed' if criteria == 0 else 'failed: ' + passMessage}\n")
        
        f.write('\n')