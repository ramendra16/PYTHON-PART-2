#ask user a number like 1256
#sum of digits----> 1+2+5+6
#logic
#num="1256",length=4
#int(num[0])---->1
# int(num[1])---->2
# int(num[2])---->5
# int(num[3])---->6
#i-----0to3
total=0
num=input("enter a number: ")
for i in range(0,len(num)):
    total+=int(num[i])
print(total)

