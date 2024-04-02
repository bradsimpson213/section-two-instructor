# XOR

# print(True ^ False)
# print(True ^ True)
# print(False ^ False)
# print(False ^ True)

# Create a function that returns the xor result of two values.
# Write your function, here.
def xor(val1, val2):
    return val1 ^ val2


# print(xor(False, False))   #>  False
# print(xor(True, False))   #>  True
# print(xor(True, True)) #>  False
# print(xor(5, 3))  #> 6
# print(xor(8, 4))  #> 12
# print(xor(2, 2))  #> 0
# print(xor(1, 2))  #> 3
# print(xor(4, 4))  #> 0
# print(bin(True))
# print(bin(False))
# 0b1
# 0b0
# print(bin(5))
# print(bin(3))
# 0b101
# 0b011
#   110
# 0b110
# print(bin(6))


# IF STATEMENTS
def breakfast(food):
    if food == "waffles": 
        print(f'{food} is my favorite breakfast!')
    elif food == "pancakes":
        print(f"{food} are a pretty good choice")
    else:
        print(f'{food}?!?! Do you even know what breakfast is?')

# breakfast("waffles")
# breakfast('pancakes')
# breakfast('cereal')


# STRINGS
meal = "breakfast"
food = "waffles"
# print(f'We are eating {food} for {meal}')
# print("we are eating {} for {}".format(food, meal))
a = "a"
b = "b"
an = "an"

# print(b + an)
# print(b + a*7)
# print(b + an*2 + a)

# print(food[-1])
# print(food[:4])

# print(food.index('a'))
# print(food.count('q'))
# print(food.split('f'))

# casting a string to a list will "split" every letter print(list(food))

# instructor = ["Brad", 'David', "John", 'Cesar']
# print(', '.join(instructor))
# print(food.upper())


# a = []
 
# if a is None:
#     print("a is None")
# else:
#     print("a is not None")  # prints "a is not None"


# STRING PROBLEMS

def is_palindrome(string):
  return string == string[::-1]

def is_palindrome_reverse(string):
  reverse = ''.join(reversed(string))
  return string == reverse


# Recursive
#base case
if len(str) == 0:
    return str
#  recursive step (in return)
return recursive_string(str[1:]) + str[0]   


def perfect_square(num1, num2):
    return num1 / num2 == num2 and num2 * num2 == num1


def recursive_countdown(n):
  if n <= 0:
    return
  else:
    print(n)
    recursive_countdown(n-1)


import os
import time

def recursive_countdown(n):
  if n <= 0:
    os.system("clear")
    print("BOOM!")
    return
  else:
    os.system("clear")
    print(n)
    time.sleep(1)
    recursive_countdown(n-1)


recursive_countdown(5) #> 5 4 3 2 1


# Recursive fib
if n <= 1:
    return n
else:
    return (recursive_fib(n-1) + recursive_fib(n-2))


def first_before_second(s, first, second):
    return s.rindex(first) < s.index(second)


# STATEMENTS


# while i < 5:
#     if i == 3:
#         print(i, 'We have a 3!')
#     else:
#         print(i, "Not 3")
#     i += 1
    
# i = 0
# while True:


import random
import time
import os

count = 99


while count < 1000:
    os.system("clear")
    print(f"{count} little bugs in our code...")
    time.sleep(0.5)
    print(f"{count} pesky little bugs...")
    time.sleep(0.5)
    print("Take one down and patch it around...")
    time.sleep(0.5)
    new_bugs = random.randint(1, 50)
    count += new_bugs
    print(f"{count} little bugs in our code!")
    time.sleep(0.5)




# for i in range(0,5):
#     print(f'{i}. Hello, world!')
#     if i < 4:
#         # i += 1
#         continue
#     print("You printed 5 times, Goodbye!")
#     break
#     print("who wants some waffles?")


# FOR LOOPS
# foods = ['pizza', 'tacos', 'waffles', 'salad']

# for food in foods:
#     print(food)

# # print('sandwich' in foods)

# print(list(range(10,0,-1)))

# for i in range(len(foods)):
#     print(i, foods[i])


# num = 'waffle'

# try:
#     print("In the try block")
#     print(4/num)

# except ZeroDivisionError:
#     print('we can not divide by zero')

# except TypeError:
#     print("we can't do math with non numbers")

# else:
#     print("this should only print if our try works")

# finally:
#     print("We should always see this!")

# counter
# iterate - check the whole sequence
# result variable
# conditional - check if numbers next to each other are the same


def seq_of_numbers(seq):
    seq += ' '
    count = 1
    i = 0
    results = ''
    while i < len(seq)-1:   # for i in range(len(seq)-1)
        if seq[i] != seq[i+1]:
            results = results + str(count) + seq[i] + ","
            count = 1
        else:
            count += 1
        i += 1

    return results




# FUNCTIONS
def is_even(num):
    return num % 2 == 0

# print(is_even(5))

# even = lambda num: num % 2 == 0

# print(even(4))

# multiply = lambda num1, num2: num1 * num2

# print(multiply(2, 5))



y = 200
x = 'pizza'

DAYS = ["Monday", "Tueday", "Wednesday"]

def make_a_five():
    """assign a variable the value of 5"""
    # global y
    y = 10
    print(y, "Inside the function")
    y += 10
    print(y, "Second time in function")


# print(y)
# make_a_five()
# print(y)

# print(make_a_five.__doc__)

# def my_function(num, num3, num2 = 5, *args, **kwargs):
#     print(num, num2, num3)

# my_function(4, 5)

# Write your code here.
# def string_multi_print(str):        # Prints 1 concatenated string
#     return lambda i : print(str * i)


# lambda_func = string_multi_print('hello ')  # Prints "hello hello "
# lambda_func(5)
# string_multi_print('wahoo ')(3)  # Prints "wahoo wahoo wahoo "


# LISTS
foods = ["tacos", "burgers", "pizza", "wings"]

# print(foods)
# print(foods[0:3:2])
# print(len(foods))
# foods.append("steak")
# print(foods)
# foods.extend(["salad", "sloppy joes"])
# print(foods)
# foods.insert(index before, item to insert)
# foods.remove('steak')
# print(foods)

vals = [2, 4, 56, 12, 7]
vals.sort()
print(vals)
print(sum(vals))
print(min(vals))
print(max(vals))