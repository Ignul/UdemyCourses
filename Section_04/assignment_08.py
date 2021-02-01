# Assignment 8

"""

Return the sum of the numbers in the list, except ignore sections of
numbers starting with a 7 and extending to the next 8
(every 7 will be followed by at least one 8).
Return 0 for no numbers.

EXAMPLE:
sum78([1, 2, 2]) → 5
sum78([1, 2, 2, 7, 99, 99, 8]) → 5
sum78([1, 1, 7, 8, 2]) → 4

"""

def sum78(int_list):
    result = 0
    flag = True
    for item in int_list:
        if item == 7:
            flag = False
        # We need to skip adding the 8 if it's the first occurence. However if there's an 8 without 7
        # we need to add it.
        if item == 8 and flag:
            result += 8
        if item == 8:
            flag = True
            continue
        if flag:
            result += item
        if len(int_list) == 0:
            return 0

    return result

print(sum78([1, 2, 2])) # 5
print(sum78([1, 2, 2, 7, 99, 99, 8])) # 5
print(sum78([1, 1, 7, 8, 2])) # 4

#my checks
print(sum78([1,2,3,4,5,6,7,8,8,9])) # add everything, except 7,8
print(sum78([7,7,8,8,8,8,8,8])) # should be 40. (every 7 will be followed by at least one 8).

# will also check out the video solution.
