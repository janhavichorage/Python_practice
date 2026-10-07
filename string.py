
 #1.sample string
text="Welcome to IMCC"

#2.strip spaces from both sides

print("remove spaces:",text.strip())

#covert to uppercase
text.upper()
#convert tolwer case
text.lower()

#4.capitalize first letter
text=text.strip()
print("capitalize first letter:",text.capitalize)

#5.Title case(caoitalize each word)
print(text.title())

#6. Count Occurence of substring
print("letter C occures:",text.count("C"),"times in text")

#7.find the position of sub string (-1 if not found)
print("position of IMCC in text is",text.find("IMCC"))
#8 replace a substring
print(text.replace("IMCC","Python Magic"))

#9 check if string starts or ends wuth certain substring
print(text.startswith("We"))
print(text.endswith("! "))

#10 split strings into list by a delimiter
print("simple split",text.split())

#111 join the list of strings with a seprator

words=["python","is","fun"]
print(" ".join(words))