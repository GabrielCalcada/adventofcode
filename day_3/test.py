import re

def process_corrupted_memory(memory):
    # Start with mul enabled
    mul_enabled = True
    total_sum = 0
    
    # Regex pattern for valid mul instructions
    mul_pattern = re.compile(r"mul\((\d+),(\d+)\)")
    
    # Split the memory string into individual instructions
    instructions = re.split(r"[^a-zA-Z0-9(),]+", memory)
    
    for instruction in instructions:
        if instruction == "do()":
            mul_enabled = True
        elif instruction == "don't()":
            mul_enabled = False
        else:
            match = mul_pattern.match(instruction)
            if match and mul_enabled:
                a, b = map(int, match.groups())
                total_sum += a * b
                
    return total_sum

# Example memory input
path = '/home/gabriel/adventofcode/day_3/'

file = open(path+'puzzel_input_part_two.txt', 'r')
#file = open(path+'test_puzzel_input_part_two.txt', 'r')

puzzel = file.read()

result = process_corrupted_memory(puzzel)
print("Sum of results:", result)
