#what does this program do?
# This program examines the list
# given to it and drops the members
# of the first list into the second 
# list and displays it.
# Of course, it does not drop duplicate 
# members in the second list
lst1=[1,2,3,1,2,3,4,5,6,7,8,9,0,4,5,6,7,8,9]
lst2=[]
for i in lst1:
    if i not in lst2:
        lst2.append(i)
print(lst2)