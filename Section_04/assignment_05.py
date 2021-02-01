
# Assignment 5

"""
Define a method that accepts a list as an argument
and returns True if one of the first_folder ( ?????? need to watch the video ) 4 elements
in the list is a 6. The list length may be less than 4.


first3([1, 2, 6, 3, 4]) → True
first3([1, 2, 3, 4, 6]) → False
first3([1, 2, 3, 4, 5]) → False

"""

def first3(int_list):
    for index, item in enumerate(int_list):
        if index < 4 and item == 6:
            return True
    return False

print(first3([1, 2, 6, 3, 4]))
print(first3([1, 2, 3, 4, 6]))
print(first3([1, 2, 3, 4, 5]))

# own tests
print(first3([0,1,2,3,4,5,6,6,6]))
print(first3([6]))




