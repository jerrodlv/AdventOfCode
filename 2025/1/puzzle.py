min_num = 0
max_num = 99
starting_num = 50
input_file_path = 'input.txt'

#function to rotate the wheel
def rotate_wheel (current_pos, steps, direction):
    new_pos = None
    if direction == 'R':
        new_pos = (current_pos + steps) % 100 #number must be between 0-99. Modulo operator used to wrap around
    elif direction == 'L':
        new_pos = (current_pos - steps) % 100
    return new_pos

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
            numRotationSteps = line [1:].strip()
            #print(numRotationSteps)
            position = rotate_wheel(position, int(numRotationSteps), rotationDirection)
            if position == 0:
                total = total + 1
except FileNotFoundError:
    print(f"Error: The file '{input_file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

print(f"The total times the position ended at 0 was {total}.")