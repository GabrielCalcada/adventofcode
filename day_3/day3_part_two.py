import numpy as np
import re 

path = '/home/gabriel/adventofcode/day_3/'

file = open(path+'puzzel_input_part_two.txt', 'r')
#file = open(path+'test_puzzel_input_part_two.txt', 'r')

puzzel = file.read()

def mult(tpl):
    return int(tpl[0])*int(tpl[1])

do =  list(re.finditer(r'do\(\)', puzzel))
dont =  list(re.finditer(r"don't\(\)", puzzel))

muls = list(re.finditer(r'mul\((\d{1,3}),(\d{1,3})\)', puzzel))

#print(dont[0].start())

cont = 0
aux = []


print(len(dont))
print(len(muls))
print(len(do))
mul = []
for match in muls:
    mul.append(match.group(0))
    
aux = mul[muls[0].end() < dont[0].start()]

print(aux)
#for match in do:
#    print(f"Match: {match.group(0)}")
#    print(f"Start index: {match.start()}")
#    print(f"End index: {match.end()}")
#    print()

#print(dont)

#mult_muls = map(mult, muls)

#print(sum(list(mult_muls)))


#print(map_muls)