#empty list

my_list=[]
print(my_list)

#with items

fruits=["apple","banana","cherry"]
print(fruits)

#to accsess list element useindex 
#positive numbers indicate from start negativre numbers indicate index from 
#0 is first elemet amd -1 is last 



#append item in list

colors=["red","blue"]
colors.append("green")
print('after adding at last',colors)


#functions

#length

numbers=[1,2,3,4,5,6,7,5,9]
print("no.of items in the list are",len(numbers))

#sum

print("sum of the numbers",sum(numbers))

#sorting

print("list in asc order",sorted(numbers))
print("list on dsc order",sorted(numbers,reverse=True))


#create a list of 10 numbers and display the sum oflast 4 elememets 
# remove the items from the list located at second amd 5th positin
# print the diff of hignest amd lowest numbers of the list
# append a new element in a list which is half of items located in 3rd position of the list

list=[1,4,5,6,7,8,9,6,4]
print(sum(list.index(-1,4)))