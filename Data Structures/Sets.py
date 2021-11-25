"""sets are represented with {} or set() that hols various values. Sets are:
- Unordered
- Unique - no duplicates
- Can carry any type but no mutable elements like lists, sets or dicts but can carry tuples"""
#examples:
#to create an empty set:
a = set() #empty {} will be assumed as dicts

#Modify a set .add()
"""sets are mutable (can be changed) but since they're unordered indexing is not supported
"""
mySet = {45, 66, 78, 99}
mySet.add(55)
print(mySet) # will add 55 to the end

mySet.update([34, 55, 23])

#removing Items .discard() or .remove()
mySet = {45, 66, 78, 99}
mySet.discard(66) #will remove 66 from mySet
mySet.remove(45) #will remove 45
"""The diff btw .discard() and .remove() is that discard won't send an error 
if number not present but remove() will""" 

#remove and return:
""".pop() can be used but item random, .clear() will clear a set"""

#Unite | or x.union(y)
seta = {1, 2, 3, 4, 5}
setb = {9, 11, 23, 56}
print(seta|setb) #will unite a and b
unitedSet = seta.union(setb)
print(unitedSet) # will do the same thing

#Intersection & or x.intersection(y)
"""To find common items in different sets"""
seta = {1, 2, 3, 4, 5, 11}
setb = {9, 11, 23, 56, 5}
print(seta & setb) #will print items that are both in a and b {5, 11} in this ex
intersectedSet = seta.intersection(setb)
print(intersectedSet)

#difference btw sets - or x.difference(y)
"""To find the difference between two sets"""
seta = {1, 2, 3, 4, 5, 11}
setb = {9, 11, 23, 56, 5}
print(seta - setb) #will print what's not in setb
differenceSet = seta.difference(setb)
print(differenceSet)

#Symmetric difference ^ or x.symmetric_difference(y)
"""To find what's not in each set"""
seta = {1, 2, 3, 4, 5, 11}
setb = {9, 11, 23, 56, 5}
print(seta ^ setb) #will print what's not in BOTH sets
SdifferenceSet = seta.symmetric_difference(setb)
print(SdifferenceSet)

#Summary of above and more functions that can be used with sets
"""
add():                Adds an element to the set
clear():              Removes all elements from the set
copy():               Returns a copy of the set
difference():         Returns the difference of two or more sets as a new set
difference_update():  Removes all elements of another set from this set
discard():            Removes an element from the set if it is a member. (Do nothing if the element is not in set
intersection():       Returns the intersection of two sets as a new set
intersection_update():Updates the set with the intersection of itself and another
isdisjoint():         Returns True if two sets have a null intersection
issubset():           Returns True if another set contains this set
issuperset():         Returns True if this set contains another set
pop():                Removes and returns an arbitrary set element Raises KeyError if the set is empty
remove():             Removes an element from the set. If the element is not a member, raises a KeyError
symmetric_difference():Returns the symmetric difference of two sets as a new set
symmetric_difference_update(): Updates a set with the symmetric difference of itself and another
union():              Returns the union of sets in a new set
update():             Updates the set with the union of itself and others"""
