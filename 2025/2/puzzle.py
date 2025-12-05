input_file_path = 'input.txt'
rangeDelimiter = '-'
lineDelimiter = ','
totalSumOfIDs = 0  #var to store our mathed numbers in at the end



with open(input_file_path, 'r') as file:
    print("\nFile content (using readlines()):")
    file_content_string = file.read()
    # split the file into lines based on lineDelimiter
    fileNewLines = file_content_string.replace(lineDelimiter, '\n')
    #print(fileNewLines)
    #for each line, we need to split the range into two numbers based on the range delimitter, then check each number in the range to see if the first half matches the second half
    for line in fileNewLines.splitlines():
        parts = line.split(rangeDelimiter)
        r0 = int(parts[0])
        r1 = int(parts[1])
        for i in range(r0, r1 + 1, 1): 
            numlen = len(str(i))





            if numlen % 2 == 0:
                half = int(numlen / 2)
                firstHalf = str(i)[0:half]
                secondHalf = str(i)[half:numlen]
                if firstHalf == secondHalf:
                    print(f"Found matching number: {i}")
                    totalSumOfIDs = totalSumOfIDs + int(i)
                    print(f"Current total sum of matching IDs: {totalSumOfIDs}")
    print(f"The total sum of all matching IDs is {totalSumOfIDs}.")



