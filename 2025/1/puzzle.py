min_num = 0
max_num = 99
starting_num = 50
input_file_path = 'input.txt'

try:
    # 
    with open(input_file_path, 'r') as file:
        print("\nFile content (using readlines()):")
        lines = file.readlines()
        position = starting_num
        total = 0
        for line in lines:
            rotationDirection = line[0:1].strip()
            #print(rotationDirection)
            numRotationSteps = int(line[1:].strip())
            #print(numRotationSteps)
            for step in range(numRotationSteps):
                if rotationDirection == 'R':
                    position = position + 1
                    if position > max_num:
                        position = min_num
                elif rotationDirection == 'L':
                    position = position - 1
                    if position < min_num:
                        position = max_num
                if position == 0:
                    total = total + 1
except FileNotFoundError:
    print(f"Error: The file '{input_file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

print(f"The total times the position ended at 0 was {total}.")