#create a list of 10 numbers and display the sum oflast 4 elememets 
list=[1,4,5,6,7,8,9,6,4,8]
print(sum(list[-4:]))
# remove the items from the list located at second amd 5th positin
print(list.remove(4))
print(list.remove(7))
print(list)
# print the diff of hignest amd lowest numbers of the list
highest_number=max(list)
print(highest_number)

smallest_number=min(list)
print(smallest_number)

diff=highest_number-smallest_number
print(diff)

# append a new element in a list which is half of items located in 3rd position of the list

list.append()