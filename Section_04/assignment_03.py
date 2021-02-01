# Assignment 3

"""
Given a list of ints, return True if the sequence of numbers 1, 2, 3
appears in the list anywhere, false otherwise.

sequence([1, 1, 2, 3, 1]) → True
sequence([1, 1, 2, 4, 1]) → False
sequence([1, 1, 2, 1, 2, 3]) → True
sequence([1, 2]) → False
sequence([]) → False
"""

# There's probably an easier solution. Will check it out.
def sequence(int_list):
    for item in range(2, len(int_list)):
        if int_list[item-2] == 1 and int_list[item-1] == 2 and int_list[item] == 3:
            return True
    return False

print(sequence([1, 1, 2, 3, 1]))
print(sequence([1, 1, 2, 4, 1]))
print(sequence([1, 1, 2, 1, 2, 3]))
print(sequence([1, 2]))
print(sequence([]))