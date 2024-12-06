list1= [[1, '1', 1], [2,'2',2], [3,'3',3]]
outlst = [' '.join([str(c) for c in lst]) for lst in list1]
for i in outlst:
    print(i)
# print(outlst)