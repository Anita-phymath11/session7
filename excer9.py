#what does this program do?
# This program takes a range from
# the user and numbers in this
# range are divisible by 15 and 
# shows their number.
lst=[]

rng=int(input("enter a number: "))
rng2=int(input("enter another number: "))
for i in range(rng,rng2+1):
    if i%15==0:
        lst.append(i)
        
print(lst)
print(len(lst))

    
    
