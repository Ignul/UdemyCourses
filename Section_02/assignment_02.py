# Assignment 2:
"""
Using some of the collection data types we learned about
in the course so such as a list and dictionary, create a
data structure that best represents the following scenario:

Tom has a salary of 20000 and is 22 years old. He owns a few items such as
a jacket, a car, and TV. Mike is another person who makes 24000 and is 27 years old
who owns a bike, a laptop and boat.
"""

# your code below:

people_dict = {'p1': {'name': 'Tom',
                    'salary': 20000,
                    'age': 22,
                    'items': ['jacket', 'car', 'TV']
                    },
               'p2': {'name': 'Mike',
                    'salary': 24000,
                    'age': 27,
                    'items': ['bike', 'laptop', 'boat']
                    }
               }

print(people_dict['p1']) # ['name'] or any other key and you'll get the value.
print(people_dict['p2'])








































# Solution

# my_list = [{'Tom': {'salary': 20000, 'age': 22, 'owns': ['jacket', 'car', 'TV']}},
#            {'Mike': {'salary': 24000, 'age': 27, 'owns': ['bike', 'laptop', 'boat']}}]
