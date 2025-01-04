# Part 1 
# Scan the corrupted memory for uncorrupted mul instructions. What do you get if you add up all of the results of the multiplications?
import re

f = open('./data/day3.txt','r')
df = f.read()
pairs = re.findall(r'mul\((\d+),(\d+)\)',df) # capture group digits

sum = 0
for pair in pairs:
    product = int(pair[0]) * int(pair[1])
    sum = sum + product

print('Part 1: ' + str(sum))


# Part 2
# what do you get if you add up all of the results of just the enabled multiplications?
part2 = re.findall(r"do\(\)|don\'t\(\)|mul\(\d+,\d+\)",df) # capture group digits
go = 1
sum2 = 0
for item in part2:
    if item == "don't()":
        go = 0
    elif item == "do()":
        go = 1
    else:
        list = item[4:-1].split(',')
        product = int(list[0]) * int(list[1]) * go
        sum2 = sum2 + product

print('Part 2: ' + str(sum2))