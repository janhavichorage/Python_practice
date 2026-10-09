# Continue skips current iteration

print("output of for loop")
for  i in range(5):
    if i==2:
        continue
    print(i)

# Break for exiting from  loop

print("output of for loop")
for  i in range(5):
    if i==2:
        break
    print(i)

#loop else
print("output of for loop with else")
for i in range(3):
    print (i)
else:
    print("loop finished without break")