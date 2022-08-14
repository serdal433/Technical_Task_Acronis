# creating an empty list
lst = []
# number of elements as input
n = int(input("Enter number of iteration : "))

# iterating till the range
for i in range(0, n):
    lst += (list(map(int, input().split(' '))))
print("\nMerged iteration : ", lst)
lst.sort()
print("\nSorted Merged iteration : ", lst)
