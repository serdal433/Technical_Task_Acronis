

Iteration1 = [1, 2, 3, 4, 5]
Iteration2 = [6, 7, 8, 9, 10]
Iteration3 = [3, 7, 4, 9, 5]
Iteration = Iteration1 + Iteration2 + Iteration3
print("\nMerged Given Iteration : ", Iteration)

for k in range(len(Iteration)):
    for m in range(len(Iteration)-1):
      if Iteration[m] > Iteration[m+1]:
        Iteration[m], Iteration[m+1] = Iteration[m+1], Iteration[m]
print("\nSorted Merged Iteration : ", Iteration)
