info={
    "key" : "value",
    "name" : "hiral",
    "learning" : "coding",
    "age" : 35,
    "is_adult" : True,
    "marks" : 94.4,
    "subjects" : ["Python","C","Java"],#List
    "topics" : ("Dictionary","Set"), #Tuple
    #Lists and dictionary cannot be used as key
    12 : 12,
    12.99 : 94.8,
    #Dictionary is mutable. So cannot be used as a key
    #Whereas Tuple is non-mutable so can be used as a key
    #They are unordered    
}

print(info)
print(type(info))

print(info["name"])
print(info["age"])
print(info["is_adult"])
print(info["subjects"])
print(info["topics"])

info["name"]="shraddha" #overwrite
info["surname"]="kanakhara"
print(info)

null_dict={}
null_dict["name"]="hiral"
print(null_dict)

#for nesting a dictionary we can make a value a new dictionary

student={
    "name" : "rahul kumar",
    "subjects" : {
        "physics" : 97,
        "chemistry" : 92,
        "maths" : 98,
    }
}

print(student)
print(student["subjects"])
print(student["subjects"]["chemistry"])

print(list(student.keys()))#dict_keys(['name', 'subjects']) returns in the form of list. Only outer keys are considered in nested dictionary
print(len(student))
print(list(student.values()))#returns values
pairs = list(student.items())#returns key value pairs as tuples
print(pairs[0])

#print(student["name2"])#error
#print(student.get("name2"))#no error -> None

student.update({"city" : "Delhi"})#Update Dictionary
#You can add a new dictionary with multiple values too
#student.update({"name" : "Neha"}) Dictionary key will get updated