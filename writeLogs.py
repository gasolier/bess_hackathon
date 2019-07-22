def write_logs(test_results):
    # Write to a logs.txt file
    f = open("logs.txt", "w+")

    for result in test_results:
        # print(resultType)
        fileTested = result["fileTested"]
        f.write(f'{fileTested}\n')
        
        testNum = 0
        failedNum = 0
        #print(result)
        for test in result['tests']:
            #print(test)
            testNum += 1
            fileName = test['file']
            testType = test["testType"]
            criteria = test["criteria"]
            passMessage = test["passMessage"]

            # only write failed tests to the log file
            if criteria != 0:
                failedNum += 1
                f.write(f"\tFailed Test: {testType}\n")
                f.write(f'\t\tFile: {fileName}\n')
                f.write(f'\t\tReason: {passMessage}\n')
        
        f.write(f"\tPassed {testNum - failedNum}/{testNum} tests\n")
        
        f.write('\n')