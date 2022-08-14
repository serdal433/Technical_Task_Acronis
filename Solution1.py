# creating an empty list
lst = []

# number of iteration as input
n = int(input("Enter number of iteration : "))

# iterating till the range
for i in range(0, n):
    lst += (list(map(int, input().split(' '))))

# print all the input iteration
print("\nMerged iteration : ", lst)

# sort all the input iteration
lst.sort()

# print all the sorted iteration
print("\nSorted Merged iteration : ", lst)
