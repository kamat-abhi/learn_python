list1 = [1,2,3]
list2 = list1
list1.append(4)
print(list2)
list2 = list1[:]
list1.append(5)
print(list2)