# safe if both of the following are true:
# The levels are either all increasing or all decreasing.
# Any two adjacent levels differ by at least one and at most three.
import polars as pl

df = pl.read_csv('./data/day2.txt', separator='\t', has_header=False)

def check_line(list_line):
    line_sum = 0
    for index in range(len(list_line)-1):
        difference = int(list_line[index]) - int(list_line[index + 1])
        if abs(difference) >=1 and abs(difference) <=3: # difference is okay
            if difference < 0: # negative pass
                line_sum = line_sum - 1
            if difference > 0: # positive pass
                line_sum = line_sum + 1
        else:
            continue
    check = abs(line_sum) == len(list_line) - 1
    return check

pass_count = []
for line in df['column_1']:
    list_line = line.split(' ')
    check = check_line(list_line)
    pass_count.append(check)

print('Part 1: ' + str(sum(pass_count)))

# Part 2 
# tolerate a single bad level in what would otherwise be a safe report.
pass_count2 = []

for line in df['column_1']:
    list_line = line.split(' ')
    for index in range(len(list_line)):
        new_list = list_line[:index] + list_line[index+1:] # removing one item from list
        check = check_line(new_list)
        if check == True:
            pass_count2.append(check)
            break
        else:
            continue

print('Part 2: ' + str(sum(pass_count2)))