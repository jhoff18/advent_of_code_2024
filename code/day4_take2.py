file_string =  './data/day4.txt'
f = open(file_string, "r")
data = list(map(lambda x: x[:-1], f.readlines()))
f.close()
xmas = ['X','M','A','S']
#### 
ans = 0
### down
local_ans = 0
for i in range(137):
    for j in range(140):
        if [data[i][j], data[i+1][j], data[i+2][j], data[i+3][j]] == xmas:
           local_ans+=1
print("down answer:")
print(local_ans)
ans+=local_ans

### up
local_ans=0
for i in range(139,2,-1):
    for j in range(140):
        if [data[i][j], data[i-1][j], data[i-2][j], data[i-3][j]] == xmas:
           local_ans+=1
print("up answer:")
print(local_ans)
ans+=local_ans

### left
local_ans = 0
for i in range(140):
    for j in range(139,2,-1):
        if [data[i][j], data[i][j-1], data[i][j-2], data[i][j-3]] == xmas:
           local_ans+=1
print("left answer:")
print(local_ans)
ans+=local_ans

### right
local_ans = 0
for i in range(140):
    for j in range(137):
        if [data[i][j], data[i][j+1], data[i][j+2], data[i][j+3]] == xmas:
           local_ans+=1
print("right answer:")
print(local_ans)
ans+=local_ans

### diagonal down right
local_ans=0
for i in range(137):
    for j in range(137):
        if [data[i][j], data[i+1][j+1],data[i+2][j+2], data[i+3][j+3]] == xmas:
            local_ans+=1

print("down right:")
print(local_ans)
ans+=local_ans
local_ans = 0

### diagonal up right
local_ans=0
for i in range(139,2,-1):
    for j in range(137):
        if [data[i][j], data[i-1][j+1],data[i-2][j+2], data[i-3][j+3]] == xmas:
            local_ans+=1
print("up right:")
print(local_ans)
ans+=local_ans

### diagonal down left
local_ans=0
for i in range(137):
    for j in range(139,2,-1):
        if [data[i][j], data[i+1][j-1],data[i+2][j-2],data[i+3][j-3]] == xmas:
            local_ans+=1
print("down left:")
print(local_ans)
ans+=local_ans
### diagonal up left
local_ans=0
for i in range(139,2,-1):
    for j in range(139,2,-1):
        if [data[i][j], data[i-1][j-1],data[i-2][j-2],data[i-3][j-3]] == xmas:
            local_ans+=1
print("up left:")
print(local_ans)
ans+=local_ans
print('Part 1: ' + str(ans))
