# Question 1:
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function.

def hello_name(user_name):
    """Display a greeting"""
    print("hello_" + user_name.upper() + "!")

hello_name("username")


# Question 2: 
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    """Print odd numbers from 1-100"""
    return(list(range(1,100,2)))


# Question 3:
# Please write a Python function, max_num_in_list to return the max number of a given list. 

def max_num_in_list(a_list):
    """Return the max number of a given list."""
    return(max(a_list))

list_a = [2,5,7,2,6]
print(max_num_in_list(list_a))

# Question 4: Write a function to return if the given year is a leap year. 
# A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. 
# The return should be boolean Type (true/false).


def is_leap_year(a_year):
    """Return a year, if it is a leap year."""
    if a_year%400 ==0 or a_year%100 !=0 and a_year%4== 0:
        return True
    else:
        return False

print(is_leap_year(2004))
print(is_leap_year(2013))
print(is_leap_year(3000))
print(is_leap_year(4000))


# Question 5:Write a function to check to see if all numbers in list are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list):
    """Check if the numbers in a list are consecutive numbers."""
    if sorted(a_list) == list(range(min(a_list), max(a_list)+1)):
        return True
    else:
        return False

list_one = [2,3,4,5,6,7]
list_two = [1,2,4,5]
print(is_consecutive(list_one))
print(is_consecutive(list_two))

