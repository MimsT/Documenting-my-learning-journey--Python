## Day 3

#I have been looking at some loops in functions, here are some examples of some codes I wrote:

"""In this code, I am counting how many numbers in the list (nums) are divisible by 10"""
def divisible_by_ten(nums): #define the function 
  counter = 0
  for n in nums:    #for every index(n) in (nums)
    if n % 10 == 0: # if n (each of the indices) when divided by ten, gives a remainder of 0 (meaning its even)
      counter += 1  # increment counter (add 1)
  return counter    # count the total of 'counter' in this case 3
print(divisible_by_ten([20, 25, 30, 35, 40]))  #Call theh function with a list of numbers

"""The following for is to greet everyone separately in list format"""
def say_greetings(names):
    greeting = []                   #Setting a variable
    for n in names:                 # for each index in (names)
      greeting.append("Hello, "+ n) # Add Hello, + index (each index in list of names) to the variable greeting
    return greeting                 # call the new value of the variable
print(say_greetings(["Minnie", "Fabian", "Sally"])) #call the function with a list of names

"""In the code below, the program is asked to delete the starting even numbers"""
def delete_starting_evens(lst):
      while (len(lst) > 0 and lst[0] % 2 == 0): #As long as our parameter lst has more than 1 item AND its first number is even 
    lst = lst[1:]   # then the list will now update to start from the first index (second item)
  return lst

#Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

