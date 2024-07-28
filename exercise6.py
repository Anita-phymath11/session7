# WHAT DOES THIS PROGRAM DO?
# This program creates a list 
# of numbers from 1 to 10 and adds
# a specific word to the list
# at the desired location.
#...................................
l=[]
for i in range(1,11):
    l.append(i)
l.insert(8,"bagherzadeh")
for i in(l):
    print(i,end=" ")
        
    