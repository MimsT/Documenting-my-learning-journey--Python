# Day 1

Technically this is not day 1, as I have been learning since October of 2021 (A month ago)
Today I am practising control flow: 
If, else and elif.
>Example of a simple code I created to calculate whether one is within the budget they set:

def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
  
    
  
  if budget < food_bill + electricity_bill + internet_bill + rent: 
   
    return True 
  
  else: 
       
    return False

print(over_budget(100, 20, 30, 10, 40))

print(over_budget(80, 20, 30, 10, 30))

 - Calling the functions at the end with the chosen values
 - Getting a different boolean depending on the input called
 

>Also using modulo operator:

def divisible_by_ten(num):
  
  if num % 10 == 0:

    return True 
  else:

    return False


print(divisible_by_ten(20))

print(divisible_by_ten(25))