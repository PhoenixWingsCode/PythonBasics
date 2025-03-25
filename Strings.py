random1="This is a string"
random2='This is a string'
random3="""This is a string"""

random4="This is a string.\nWe are creating in python"
print(random4)

random5="This is a string.\tWe are creating in python"
print(random5)

str1="hello"
str2="world"
print("Concetination :",str1+str2)
print("Length : ", len(str1))

ch=str1[2]
print("Indexing:",ch)

print("Slicing : ",str1[1:4])#ending index not included

print(str1[0:len(str1)])#includes last index

print(str1[1:])#automatically goes till end
print(str1[:len(str1)])#automatically counts from start

#Backward indexing
#It starts from -1 as the last index
#Here also last index not included

print(str1[-3:-1])

print(str1.endswith("lo"))#Gives result in true or false
print(str1.capitalize())#Capitalizes first letter. Doesn't make changes in original string
print(str1.replace("h","t"))
print(str1.replace("hello","tello"))
print(str1.find("e"))#first index of first occurence.If no match then -1

str=str1+ " " + str2
print(str.find("o"))