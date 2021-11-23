"""Try and except is a function used to handle errors in our code, it is used to anticipate 
errors and catch mistakes so that a simple error doesn't crash our whole program.
Except can either be used as a stand-alone function or used with a specific error.
The code that we are running must be indented to be inside the try - except"""

#Example 1 of a try and except
try:
    value1 = int(input("please enter a first number to divide:"))
    value2 = int(input("Please enter the second number to divide:"))
    print(value1/value2)
except ZeroDivisionError:               #this will catch division by 0
    print("You cannot divide by zero")
except ValueError:               
    print("Invalid character, please insert a number")
"""In the code above, I caught 2 errors, one for if the input is different charachters 
than numbers (ValueError) and the other if the peron tries to divide by zero (ZeroDivisionError)"""

#Example 2:
try:
    answer1 = int(input("enter a number"))
    answer2 = int(input("enter a second number"))
    print(answer1 / answer2)
except ZeroDivisionError as err:
    print(err)
"""The above shows that one can store the except value as a variable (in this case err) and when
printed, it will show the actual error (in this case: Division By Zero)"""

#Example 3:
try:
    x = int(input("Enter a number up to 100 to start the counter: "))
    inputs = x
    if x < 100:
        for i in range (x + 1):
            print(i, "going up!")
            if i == x:
                print("done")
    else:
        print("This is over 100, please try again.")
except ValueError:
    print(" This is an invalid input, please enter a number")
# Method 2 using range to make a counter :
x = int(input("Enter a number up to 100 to start the counter: "))
counter = range(0, x + 1)
list_a = list(counter) 