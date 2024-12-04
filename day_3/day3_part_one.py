import numpy as np
import re 

path = '/home/gabriel/adventofcode/day_3/'

file = open(path+'puzzel_input_part_one.txt', 'r')
#file = open(path+'test_puzzel_input_part_one.txt', 'r')

puzzel = file.read()

def mult(tpl):
    return int(tpl[0])*int(tpl[1])

muls = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', puzzel)


mult_muls = map(mult, muls)

print(sum(list(mult_muls)))


#print(map_muls)