# what does this program do?
# This program deletes the members
# of my list one by one. and 
# it shows in two ways.
#////////////////////////////////////////
l2=[]
l3=[]
l=["Anita","Hana","Karami","behnamjoo","is 13 years old","is 2 years old"]
# print(len(l))
for i in range(0,len(l)):
    if i%2==0:
        l2.append(l[i])
    else:
        l3.append(l[i])
print(l2)
print(l3)