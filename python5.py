#ٌ what does this app do?
#This program changes 6 
# in a list to python and
# then displays it.
Q = ([1, 2, 3], [[4, 5, 6]], [7, [8], 9])

lst = list(Q)
# print("lst ",lst[1])

lst[1][0][2]="python" 
tup=tuple(lst)

print(tup)