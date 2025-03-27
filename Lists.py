marks=[94.4, 87.5, 95.2, 66.4, 45.1]
print(marks)
print(len(marks))
print(marks[0])

student=["karan",95.4,17,"Delhi"]
print(student)

#Strings are immutable that is they can be accessed but not changed
#Lists are mutable that they can be accessed and changed

print(student[0])
student[0]="Arjun"
print(student)

#lists can have multiple data types in same variable

print(marks[1:4])
print(marks[:4])
print(marks[0:])

print(marks[-3:-1])

marks.append(13.1)#When it returns nothing then it prints None
print(marks)

marks.sort()#Generally in ascending order
print(marks)

marks.sort(reverse=True)#sorts in descending order
print(marks)

characters=['a','e','b','x','v']
characters.sort()
print(characters)

characters.sort(reverse=True)
print(characters)

marks.reverse()
print(marks)

marks.insert(1,26.2)#inserts element at an index
print(marks)

list=[2,1,3,1]
list.remove(1)
print(list)

list.pop(1)
print(list)

tuple=(2,1,3,1)#Tuples are immuatable
print(type(tuple))
print(tuple[0])
#tuple[0]=5 Cannot be done here

#tuple=() This is an empty tuple it is valid. Result is ()
#tuple=(1,) This is also a tuple if not with a comma then treated as an integer

#print(tuple[1:3])
tuple.index(3)#Gives index of the element 
tuple.count(1)#Counts the number of occurences of the element 