# TUPLES

tup = ('red', 'blue')
tup += 'green', 'orange'
# print(tup)
# print(tup[1])

# tup2 = 'Brad', "John", 'Cesar'
# print(tup2)

# EMPTY TUPLE
tup3 = ()
# SINMGLETON TUPLE
tup4 = 1,
tup5 = (2,)


def sum_and_average(lst):
    list_sum = sum(lst)
    average = list_sum / len(lst)
    return (list_sum, average)

# print(sum_and_average([1, 2, 3, 4]))

DAYS = ("Mon", "Tue", "Wed", "Thur", "Fri")

sorted_days = sorted(DAYS)
# print(tuple(sorted_days))
# print(DAYS[2:4])

def function(num, *args):
    for arg in args:
        print(arg)

# function(1, 2, 3)

# TUPLE Problem #6
def compare(val):
    return val[1]


def index_sort(tuple_list):
    tuple_list.sort(key= compare) # lambda x: x[1]
    return tuple_list


# RANGES & ENUMERATE
values = range(10, 0, -1)
# print(list(values))

lunch = ['wings', 'pizza', 'sandwich']
carols = ["Deck the halls", "Silent Night", "Jingle Bells"]

# for i in range(len(lunch)):
#     print(lunch[i])

# print(list(enumerate(lunch)))

# for i, v in enumerate(lunch, 1):
#     print(f'{i}. {v}')



# Write your function, here.
def factorial(n):
  total = 1
  for i in range(1, n + 1):
    total *= i
  return total


def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n * recur_factorial(n - 1)


print(recur_factorial(1))     #> 1
print(recur_factorial(8))     #> 40320
print(recur_factorial(12))    #> 479001600

# Problem 4 - Check Nested Arrays
# Your code, here.

def can_nest(list1, list2):
    list1_min = min(list1)
    list1_max = max(list1)
    list2_min = min(list2)
    list2_max = max(list2)
    return list1_min > list2_min and list1_max < list2_max


# DICTIONARIES

meals = {
    'breakfast': 'coffee',
    'lunch': 'wings',
    'dinner': 'pizza',
    'dessert': 'ice cream',
    4: 'meals',
    True: 'even more meals',
    'second breakfast': 'apple'
}

# print(meals)
# print(meals.get('second breakfast', "Key not in dictionary!"))

# if meals.get("second breakfast") is None:
#     meals["second breakfast"] = 'apple'
# else:
#     print("Key already exists")

# print(meals)

# meals['second breakfast'] = 'taters'

# print(meals)
# del meals[4]
# print(meals)
# meals[1] = 'apple'
# print(meals)
# meals[True] = 'cake'
# print(meals)
# meals.update(new_dict)  will concat dictionaries

# print("binner" in meals) 

# print(meals.keys())
# print(meals.values())
# print(meals.items())

# for k, v in meals.items():
#     print(f'{k}: {v}')

# for val in meals.values():
#     print(val)


# ARGS / KWARGS

def sum (num1, num2, *args, **kwargs):
    total = num1 + num2
    print("args", args)
    for val in args:
        total += val
    print("kwargs", kwargs)
    for more_vals in kwargs.values():
        total += more_vals
    return total

# print(sum(10, 15, 25, 30, num5=15, num6=20))

lst1 = ['a', 'b', 'c']
lst2 = [1, 2, 3]
lst3 = [*lst1, *lst2]
# print(lst3)

dict1 = {
    "breakfast": 'eggs',
    "lunch": 'wings',
    "dinner": 'pizza'
}

dict2 = {**dict1}

# print(dict2)

# Write your code here.
def merge_lists(list_1, list_2):
  # return dict(zip(list_1, list_2))
  return_dict = {}
  for index, value in enumerate(list_1):
    return_dict[value] = list_2[index]

  return return_dict
  
def merge_lists2(list_1, list_2):
    merged_list = []
    for index in range(len(lst1)):
        merge_tuple = (lst1[index], lst2[index])
        merged_list.append(merge_tuple)
    return dict(merged_list)


lst1 = ['a', 'b']
lst2 = [1, 2]
merged_dict = merge_lists(lst1, lst2)
print(merged_dict)      # { 'a': 1, 'b': 2 }



# SETS
# new_set = set()
# another_set = {1, 2, 3}
# print(new_set)
# print((another_set))

# list1 = [1, 2, 2, 3, 3, 4, 5, 6, 6, 7]
# print(set(list1))

# string1 = "hello"
# print(set(string1))

my_set = {1, 2, 3, 4}
print(1 in my_set)
# print(my_set)
# # my_set.add(5)
# # print(my_set)
# my_set.update([5, 6])
# my_set.remove(2)
# print(my_set)


# UNION
# print(a | b)
# print(a.union(b))

# INTERSECTION
# print(a & b)
# print(a.intersection(b))

# DIFFERENCE
# print(a - b)
# print(a.difference(b))
# print(b - a)

a = {0, 1, 2, 3}
b = {0, 1, 5, 6}

# SYMMETRIC DIFFERENCE
# print(a ^ b)
# print(a.symmetric_difference(b))

# One possible solution
def check_binary(str):
    str_set = set(str)
    return str_set == ({ '0', '1' } or { '1' } or { '0' })

# Using .issubset
def check_binary2(str):
    str_set = set(str)
    return str_set.issubset({ '0', '1' })
    
def check_binary(str):
    binary_set = set(str)
    list_of_sets = [{"0", "1"}, {"0"}, {"1"}]
    return binary_set in list_of_sets

def check_binary(string):
    converted_set = set(string)
    binary_set = {"0", "1"}
    if converted_set ^ binary_set:
        return False
    else: 
        return True



# BUILT IN FUNCTION
names = ["JAMES", 'julie', 'Ana', "Ria"]
sorted_names = sorted(names, key= lambda x: x.lower(), reverse=True)
# print(sorted_names)


# ALL ANY

# all is happy if nothing inside is falsy, 
# any is happy if at least one thing is truthy

test = ['', False, 0]
test2 = {}
# print("all", all(test2))
# print("any", any(test2))

# FILTER
scores = [90, 86, 75, 91, 62, 99, 88, 90]
only_as = filter(lambda num: num >= 90, scores)
list_set = set(only_as)
list_list = list(list_set)
# print(list_set)
# print(list_list)


# MAP
def get_grade(num):
    if (num >= 90):
        return "A"
    elif (num <90 and num >= 80):
        return "B"
    elif (num < 80 and num >= 70):
        return "C"
    elif (num < 70 and num >= 60):
        return "D"
    else:
        return "F"

mapped_grades = map(get_grade, scores)
# print(scores)
# print(list(mapped_grades))

# ZIP
scores = [90, 86, 75, 91, 62, 99, 88, 90 ]
grades = ["A", "B", "C", "A", "D", "A", "B", "A"]
combined = zip(scores, grades)
combined_list = list(combined)
combined_dict = dict(combined_list)
# print(combined_list)
# print(combined_dict)


# REMOVE DUPLICATES SOLUTION EXPLAINED

def get_unique_models(phone_list):
    just_models = map(lambda phone: phone["model"], phone_list)
    print(list(set(just_models)))
    

def get_unique_models(phone_list):
    seen = []
    return filter(lambda phone: seen.append(phone['model']) is None if phone['model'] not in seen else False, phone_list)
    
    # so what is going on here in the filter method???
    # think of the lambda statement being written like this...
    if phone['model'] not in seen:
        return seen.append(phone['model']) is None
    else:
        return False
    #
    # Because this is a callback in a filter, it needs to return True or False
    # to determine if the value gets added to our filtered list
    #
    # In the else, we return False, makes sense...
    # The append method does not have a return, but we know that if a
    # function does not have a set return value, it returns None!
    # So we check if the return value is None, which will evaluate to true!



# COMPREHENSIONS
my_list = [1, '2', 'THREE', True, None]
my_list_copy = [item for item in my_list]
# print(my_list_copy)

# COPY without a COMPREHENSION
my_list_copy = []
for item in my_list:
    my_list_copy.append(item)
# print(my_list_copy)

nums = [-5, 11, 10, 14]
# mapped_nums = map(lambda num: num * 2, nums)
# print(list(mapped_nums))
mapped_nums = [ num * 2 for num in nums]
# print(mapped_nums)
filter_nums = [num for num in nums if num > 0]
# print(filter_nums)
mapped_and_filtered_nums = [num * 2 for num in nums if num > 0 ]
# print(mapped_and_filtered_nums)

number_dictionary = { num: num**2 for num in range(5) }
# print(number_dictionary)

breaks = {
    'lunch': 2,
    'afternoon': 6,
    'EOD' : 7
}
# print(breaks)
# daylight_savings = {k: v + 1 for k, v in breaks.items() }
# print(daylight_savings)