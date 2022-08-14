
# creating an empty list
lst = []
# number of elements as input
n = int(input("Enter number of iteration : "))

# iterating till the range
for i in range(0, n):
    lst += (list(map(int, input().split(' '))))
print("\nMerged Input Iteration : ", lst)

for k in range(len(lst)):
    for m in range(len(lst)-1):
       if lst[m] > lst[m+1]:
           lst[m], lst[m+1] = lst[m+1], lst[m]
print("\nSorted Merged Iteration : ", lst)
