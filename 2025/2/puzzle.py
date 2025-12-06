input_file_path = 'input.txt'
rangeDelimiter = '-'
lineDelimiter = ','
totalSumOfIDs = 0  #var to store our mathed numbers in at the end


def part2_valid(id_str: str) -> bool:
    id_str = str(id_str)
    n = len(id_str)
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            if id_str == id_str[:i] * (n // i):
                return False
    return True

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
            if not part2_valid(i):
                print(f"Matched ID: {i}")
                totalSumOfIDs = totalSumOfIDs + i
                print(f"Current total sum of IDs: {totalSumOfIDs}")
    print(f"The total sum of all matching IDs is {totalSumOfIDs}")



