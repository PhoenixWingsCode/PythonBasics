#set is the collection of the unordered items
#each element is the set must be unique & immutable
#all data types can be stored except list and dictionary

collection = {1,2,3,4,"hello","world"}
print(collection)
print(type(collection))
print(len(collection))#duplicate values not counted

#collection = {} empty dicitionary
collection = set() #empty set

#set is mutable
#set elements is immutable

empty_collection = set()
empty_collection.add(1)
empty_collection.add(2)
empty_collection.add(2)
empty_collection.add("hiral")
empty_collection.add((1, 2, 3))

print(empty_collection)

empty_collection.remove(1)#It gives keyerror. Keyerror means that key doesn't exist
print(empty_collection)

print(len(empty_collection))
empty_collection.clear()
print(len(empty_collection))

spellings={"hello","hiral","world","coding","python"}
print(spellings.pop())#random value pop up
print(spellings.pop())#random value pop up

set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1.union(set2))
print(set1.intersection(set2))