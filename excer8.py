#What does this program do?
# This program stores even 
# numbers from 1 to 100 in a 
# variable called L1 and odd numbers
# from 1 to 100 in a variable 
# called L2 and displays them.
#....................................
l1=[]
l2=[]
a=0
while a<100:
    a+=1
    if a%2==0:
        l1.append(a)
    elif a%2!=0:
        l2.append(a)
print("l1=",l1,sep=" ")
print("l2=",l2,sep="")
