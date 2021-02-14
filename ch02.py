#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 18:53:47 2021

@author: damascus
"""

for i in [1, 2, 3, 4, 5]:
    pass
   #  print(i)
    for j in [1, 2, 3, 4, 5]:
        pass
        # print(j)
        # print(i + j)
    # print(i)
        

    
# %%
# For long winded computations
long_winded_computation = (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 
                           11 + 12 + 13 + 14 + 15 + 16 + 17 + 18 + 19 + 20)

# %%

# Reading list_of_lists
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]



# %%
# blacklash that enables one to continue
two_plus_three = 2 + \
                3
                
                
# %%               

import re

my_regex = re.compile("[0-9]+", re.I)           

# %%

import re as regex


my_regex_v2 = regex.compile("[0-9]+", regex.I)

# %%

def double(x):
    z = x * 2
    return z

# print(double(2))

 # %%

names = ["Samuel", "Felicia", "Abrhama", "David", "Jordan", "Maegan", "Allysa"]
print(names[0])
print(names[0:3])   
print(names[1:-2])  

# %%

first_name = "Samuel"
last_name = "Ademola"
full_name_1 = first_name + last_name
full_name_2 = "{0} {1}".format(first_name, last_name)
full_name_3 = f"{first_name} {last_name}"

# %%

try:
    print(0 / 0)
except ZeroDivisionError:
    print("Cannot devided by zero")
    
# %%

x = [1, 2, 3]
y = [4, 5, 6]
x.extend(y)      

# %%

grades = {"Joel": 80, "Tim": 95}
print(grades["Joel"]  )    

# chuck_grades = grades["Chuck"]


try: 
    kates_grades = grades["Kate"]
except KeyError:
    print("no grade for Kate")
    
joel_has_grades = "Joel" in grades
kate_has_grades = "Kate" in grades

grades["Tim"] = 99  ## Replaces the old value
grades["Kate"] = 80

num_students = len(grades)

# %%

tweet = {
    "user" : "joelgrus",
    "text" : "Data Science is Awesome",
    "retweet_count" : 100,
    "hashtags" : ["#data", "#science", "#datascience", "#awesome", "#yolo"]
    }

tweet_keys = tweet.keys()                                   # iterable for keys
print(tweet_keys)

tweet_values = tweet.values()                               # iterable for values
print(tweet_values)

tweet_items = tweet.items()                                 # iterable for items
print(tweet_items)

true_or_fales = "user" in tweet

# %%

# Trying to count the words in a document

# word_counts = {}
# for word in document:
#     if word in word_counts:
#         word_counts[word] += 1
#     else:
#         word_counts[word] = 1
        
        
# %%

# forgivness approach
# word_counts = {}
# for word in document:
#     try:
#         word_counts[word] += 1
#     except KeyError:
#         word_counts[word] = 1
        
# %%

# third approach

# word_counts = {}
# for word in document:
#     previous_count = word_counts.get(word, 0)
#     word_counts[word] = previous_count + 1
    
# %% 

# Importing from the collections module

from collections import defaultdict

# word_counts = defaultdict(int)
# for word in document:
#     word_counts[word] += 1
    
# %%

dd_list = defaultdict(list)                                 # list() produces an empty list
dd_list[2].append(1)
print(dd_list)

# %%

dd_dict = defaultdict(dict)
dd_dict["Joel"]["City"] = "Plano"
print(dd_dict)

dd_dict["Joel"]["City"] = ["Seatle", "Austin", "Boston"]
print(dd_dict)

# %%

dd_pair = defaultdict(lambda: [0, 0])
dd_pair[2][1] = 1
print(dd_pair) 

# %%

# Counters

from collections import Counter

c = Counter({0, 1, 2, 0})
print(c)

# %% 
# from collections import Counter

# word_counts = {}
# for word, count in word_counts.most_common(10):
#     print(word, count)
    

# %%

primes_below_10 = {2, 3, 5, 7}
for n in primes_below_10:
    print(n)
    
# %%

hundreds_of_other_words = []

stopwords_list = ["a", "an", "at"] + hundreds_of_other_words + ["yet", "you"]
zip_or_not = "zip" in stopwords_list                                 # False, but will have to check every element

stopwords_set = set(stopwords_list)

zip_or_yes = "zip" in stopwords_set

# %%

x = 10

parity = "even" if x % 2 == 0 else "odd"

# %%

b = [-4, 1, -2, -3]
b_sorted = sorted(b)
b_sorted_v2 = sorted(b, key=abs, reverse=False)

# %%

assert 1 + 1 == 2

# %%

def smallest_item(xs):
    return min(xs)

assert smallest_item([10, 20, 5, 40]) == 5

# %%

families = ["Alice", "Bob", "Charlie", "Bebbie"]
for i in range(len(families)):
    print(f"families {i} is {families[i]}")
    
# %%

g = 0
for family in families:
    print(f"family {g} is {family[g]}")
    g += 1
    
# %%

for i, family in enumerate(families):
    print(f"family {i} is {family}")
    
# %%

# Zipping Iterables
list_1 = ['a', 'b', 'c', 'd', 'e', 'f', 'h']
list_2 = [1, 2, 3, 4, 5, 6, 7]

fusion_dbz = zip(list_1, list_2)
print(fusion_dbz)

print([pair for pair in zip(list_1, list_2)])

# Unziping iterables
pairs = [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5), ('f', 6), ('h', 7)]
letters, numbers = zip(*pairs)