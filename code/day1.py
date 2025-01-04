# PART 1
import polars as pl

df = pl.read_csv('./data/day1.txt', separator=' ', has_header=False)
list1 = df.sort('column_1')['column_1']
list2 = df.sort('column_4')['column_4']
print('part 1: ' + str(sum(abs(list2-list1))))

# PART 2
# Calculate a total similarity score by adding up each number in the left list after multiplying it by the number of times that number appears in the right list.

similarity_score = 0
for item in list1:
    count = 0
    for item2 in list2:
        if item == item2:
            count = count + 1
    similarity_score = similarity_score + count*item

print('part 2: ' + str(similarity_score))