# TUPLE: order (iterable), unchangable, repetable
tup1 = (1,2,3,43,2,2,3,4,5,4,3,2,2,4,4,5,3,2,1,3)
tup1 = tuple((1,2,3,43,2,2,3,4,5,4,3,2,2,4,4,5,3,2,1,3))
lst1 = list(tup1)
lst1[0] = 8
tup1 = tuple(lst1) 
# tuple is unchangeable. must change to list to access ele
tup2 = (9,)
tup1 += tup2  # append tuple
(a,b,*c) = (9,3,2,1)
print(tup1.count(2)) # count num of ele in tup
print(tup1.index(3)) # find value, return first met index
print(len(tup1)) # return tup's length
tup3 = (1,2) + (3,4) # concatenation
tup4 = (3,4)*5 #repetition
tup5 = 3 in tup1 # membership
for x in tup1: print(x) #iteration
print(c)
del tup2

#SET: unorder, unchangable (but can del or append), cant use index, ele cant repeat, sorted
set1 = {1,2,3,4,45,5,3,2,2,2}
set2 = set({"3,4,2,2,4,5,2,2,3,3,4,3,21,1,3,3"})
for x in set1: print(x) # iteration
set1.add(3) # add value into set
set1.update(set2) # add last collections
print(set1)
set1.remove(3) # remove value, raise error inexistent value
set1.discard(3) #remove value but no raise inexistent error
set1.pop() #remove randomly element
set1.clear() #remove all ele, return an empty set
set3 = set1.union(set2) # OR op
set3 = set1.intersection(set2) # AND op
set1.intersection_update(set2) # AND op, assign onto set1
set3 = set1.difference(set2) # MINUS op
set3 = set1.symmetric_difference(set2) # MINUS AND op
del set2 #remove obj

#DICTIONARY: ordered, changeable, no repeat key
# a value can have multible key, but a key cant have multible value
dict1 = {"name": "Hung", "yob": "2005"}
dict2 = dict(name = "Hung", yob = "2005")
print(dict1["name"]) # access value by key
print(dict1.get("name")) 
print(dict1.keys()) # return a list of keys
print(dict1.values()) #return a list of values
print(dict1.items()) # return a list of tuples (pair key and value)
dict1["grade"] = 12 # add new key or write onto old key
dict1.update({"name": "Hung"})
dict1.pop("name") # delete value by key
dict1.popitem() #delete last
dict1.clear() #delete whole dict, return empty dict
for key in dict1: print(key) 
for key in dict1.keys(): print(key) # get key
for key in dict1: print(dict1[key])
for x in dict1.values(): print(x)
for key, value in dict1.items(): print(key, value)
del dict1 #delete obj