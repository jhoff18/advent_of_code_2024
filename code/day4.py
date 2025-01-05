# Part 1
# horizontal, vertical, diagonal, written backwards, or even overlapping other words
import polars as pl
import re
import numpy as np

df = pl.read_csv('./data/day4.txt', separator='\t', has_header=False)
df = pl.read_csv('./data/input4.txt', separator='\t', has_header=False)

df_grid = df.select(pl.col("column_1").str.split_exact("", 139)).unnest("column_1")
df_grid_replace=(df_grid.select(pl.all().str.replace('X','1'))
                 .select(pl.all().str.replace('M','2'))
                 .select(pl.all().str.replace('A','3'))
                 .select(pl.all().str.replace('S','4'))
                 .select(pl.all().cast(pl.Int32)))
np_grid = df_grid_replace.to_numpy()

def count_XMAS(np_grid):
    count = 0
    for row in np_grid:
        strg = ''.join(str(x) for x in row).replace("0", "")
        # print(strg)
        # print(len(re.findall(r'1234', strg)))
        count = count + len(re.findall(r'1234', strg)) + len(re.findall(r'4321', strg))
    return count

## rotate 45
def rotate_45_and_count(np_grid, size = 140): # includes middle
    count = 0
    for sum in range(size):
        row = []
        for i in range(size):
            for j in range(size):
                if i + j == sum:
                    row.append(np_grid[i,j])
        strg = ''.join(str(x) for x in row).replace("0", "")
        count = count + len(re.findall(r'1234', strg)) + len(re.findall(r'4321', strg))
    return count

def rotate_45_and_count_bottom(np_grid, size = 140): # no middle
    count = 0
    for sum in range(size+1, ((size*2)+1)):
        row = []
        for i in range(size):
            for j in range(size):
                if i + j == sum:
                    row.append(np_grid[i,j])
        strg = ''.join(str(x) for x in row).replace("0", "")
        count = count + len(re.findall(r'1234', strg)) + len(re.findall(r'4321', strg))
    return count

#######
def make_top(j,n):
    i=0
    row = []
    while j <= n:
        # print(i,j)
        row.append(np_grid[i,j])
        i+=1
        j+=1
    return row

def make_bottom(i,n):
    j=0
    row = []
    while i <= n:
        # print(i,j)
        row.append(np_grid[i,j])
        i+=1
        j+=1
    return row

size=139
count_other_diag=0
for j in range(size,0,-1):
    top_line = make_top(j,size)
    bottom_line = make_bottom(j,size)
    strg_top = ''.join(str(x) for x in top_line).replace("0", "")
    strg_bottom = ''.join(str(x) for x in bottom_line).replace("0", "")
    # print(j, strg_top, strg_bottom)
    count_other_diag = count_other_diag + len(re.findall(r'1234', strg_top)) + len(re.findall(r'4321', strg_top)) + len(re.findall(r'1234', strg_bottom)) + len(re.findall(r'4321', strg_bottom))
strg_middle = ''.join(str(x) for x in make_top(0,size)).replace("0", "")
count_other_diag = count_other_diag + len(re.findall(r'1234', strg_middle))
#####

count_XMAS(np_grid) # horizontal 406  *  447 y
count_XMAS(np_grid.transpose()) # vertical 455  *  460 y
rotate_45_and_count(np_grid) + rotate_45_and_count_bottom(np_grid) # 45 degree 424  *  834 n = 839      down left, up right
print(count_other_diag) # other diagonal 849  *  821 n = 828    up left, down right 

print('Part 1: ' + str(count_XMAS(np_grid) + count_XMAS(np_grid.transpose()) + rotate_45_and_count(np_grid) + rotate_45_and_count_bottom(np_grid)  + count_other_diag)) # 2573

# too low 2559; 2562
# 2552; 2562