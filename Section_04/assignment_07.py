# Assignment 7
"""
Given 2 strings, a and b, return the number of the positions where
they contain the same length 2 substring. So "xxcaazz" and "xxbaaz"
yields 3, since the "xx", "aa", and "az" substrings appear in the same
place in both strings.

EXAMPLE:
    string_match('xxcaazz', 'xxbaaz') → 3
    string_match('abc', 'abc') → 2
    string_match('abc', 'axc') → 0

"""

def string_match(text1, text2):
    # ok so we need to know, which str is shorter for the iter count.
    # Because it won't matter if the other is longer - there won't be any matches
    iter_count = min(len(text1), len(text2))
    # how many times the 2 substrings match
    counter = 0

    # Make sure to start at 1.
    for index in range(1, iter_count):
        if text1[index-1:index+1] == text2[index-1:index+1]:
            counter += 1

    return counter

print(string_match('xxcaazz', 'xxbaaz'))
print(string_match('abc', 'abc'))
print(string_match('abc', 'axc'))

#own tests
print(string_match('abbc', 'abbc')) #should be 3
print(string_match('axcc', 'abxc')) # should be 0


