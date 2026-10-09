# print tables of  all odd numbers from 1 to 10
for num in range (1,10+1):

    if num%2!=0:
        print("printing table of",num)
        for i in range(1,11):
            print(num*i)



# create a heterogenous list of numbers and names split the list from  highest number  
#add two numbers at 3rd position and append one list and then split

list=[1,4,6,7,"janhavi","sanjana","pratik","ruturaj"]
max=0
for i in list:
    max= 
print(list.partition())




#Accsept the name  and check if  its palindrome 

name=input("Enter the name:")
if name ==name[::-1]:
    print("palindrome")
else:
    print("not palindrome")

#print sumof digits
n=(input("enter your number:"))
sum=0
for i in n:
    sum=sum+int(i)
print(sum)

 #printing pattern

n=int(input("enter input:"))
for i in range(1,n+1):
    for j in range(i):
        if i%2==1:
            print("*", end="")
        else:
            print("#",end="")
    print()



# printing pyramid
n=int(input("Enter rows"))
for i in range (1,n+1):
    for j in range (n-i):
        print(" ", end=" ")
    for j in range (i):
        if i%2==1:
            print("*",end=" ")
        else:
            print("#",end=" ")
    for j in range (i-1):
        if i%2==1:
            print("*",end=" ")
        else:
            print("#",end=" ")
    print()

#