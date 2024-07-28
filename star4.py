#what does this app do?
#This program takes 
# 5 values ​​from 
# the user and stores 
# them in three variables
# And it does not show 
# the last one as a list.
list1=[]
for i in range(5):
    names=input("enter your names...")
    list1.append(names)
name1, name2,*names=list1
print(name1)
print(name2)
for i in (names):
    print(i, end=" ")