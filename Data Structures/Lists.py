"""Lists are use to store multiple items in a single variable.
they are: """
#Changeable:
list = [2, 5, 6, 7, 8, 9]
print("Unchanged list:", list)
list[0] = 6                   #Changing first item
list[-1] = 100                #Changing last item
list[3]= 24                   #Changing 4th item
print("Changed list:", list)  
"""Code will print:
Unchanged list: [2, 5, 6, 7, 8, 9]
Changed list: [6, 5, 6, 24, 8, 100]"""

#Ordered 
"""Items will always occuppy an ordered position unless changed using .insert() to shift
items to different positions. """

#Allow duplicates
"""You can enter the same value more than once.
for example:"""
list = [2, 5, 2, 5]

#Any data type, can be mixed
"""Any type of value can be inserted.
for example:"""
list = ["Mother", 3, 8.9, 45j, True]

#List() constructor
"""The list() constructor returns a list in Python >>>"""
Text = "Python"
new_text = list(Text)
print(new_text)   #This will print: ['p', 'y', 't', 'h', 'o', 'n']

#Array index range
x[-1] #last item in array 
x[-2] #last 2 items
x[:-2] #everything except the last 2

newlist = [1, 2, 3, 5, 6, 7, 8, 9]
print(newlist[4:7]) #will print [6, 7, 8]
"""number at index 4 is 6 and the range includes UP TO BUT NOT INCLUDING index 7"""

#Checking if item is present in the list
"""This can be done in many ways, but we will use .count() as it preserves the original list.
ex:"""
list1 = [23, 45, 66, 899, 675, 67, 66, 45]
inlist = list1.count(66)
print(inlist) #will print 2 as 66 is in list1 twice

#Add stuff to the list
list1 = [23, 45, 66, 899, 675, 67, 66, 45]
list1.append(45.6) #will add 45.6 to the END of list1
list1.insert(2, 99) #first value(2) in index, 99 is the value, this will add 99 to the second index

#removing from list
list1 = [23, 45, 66, 899, 675, 67, 66, 45]
list1.remove(45) #will remove the first encounter of 45 from list
list1.clear() #will remove everything from list

#misc
list1.copy() #will make a copy of list
list1.count(45) #will count how many 45s
list1.extend([3, 4, 5]) #will concatenate lists
print(list1.index(23)) # will print 0 as its the position of 23 in list1
list1.pop(0) #will remove 23 bcs its al index 0
list1.remove(23) #will remove the first 23 from list
list1.reverse() #reverses the order of list1
list1.sort() #sorts the order of the list from smallest to largest
