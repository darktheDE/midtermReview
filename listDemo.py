lst = [0,1,2,3,4,5,67,3,2,1,2,4,5,6,8,8,9,98,6,5,3,2,3,3,4,4,5,6,67,7,88,9]
lst.insert(3, 22) # insert(index, value)
lst.append(24) # add last, value
new_lst = [ x  for x in lst if x%2 == 0] # list comprehension
lst.extend(new_lst) # add new_lst into lst
lst.remove(0) #remove(value) first met element
lst.pop(4) #remove, show value of index. 
lst.pop() #remove, show value of last ele
del lst[0] # remove element with index
lst.clear() # remove everything and return a empty list
lst.sort() # sort right onto list
lst1 = sorted(lst) # sort the sent list, return new list.
lst2 = lst1.copy()
lst2 = list(lst1) # this all "copy" mean create new memory field, the "=" op is only reference.
lst2 = lst1# this mean lst2 point to lst1 address, every change on lst2 will change lst1 as well
# 2-dim list is a list 1-dim list with each ele is a 1-dim list
print(lst)
del lst  #delete whole obj