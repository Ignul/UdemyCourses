# Assignment 6

"""
Create a function called last2 that accepts a string argument.
The function should return the count of the number of times that the last
2 characters appear in the rest of the string. You should not count
the last 2 characters as an occurrence. The last 2 characters is just the
sequence your function should look for in the remaining string.

So "hixxxhi" yields 1 (we won't count the end substring).


last2('hixxhi') → 1
last2('xaxxaxaxx') → 1
last2('axxxaaxx') → 2

"""

def last2(text):
    #Get the last 2 chars.
    last_chars = text[-2:]
    print(last_chars)
    # The input text without last 2 letters.
    stripped_text = text[:-2]
    counter = 0
    for index in range(1, len(stripped_text)):
        if last_chars == text[index-1:index+1]:
            counter += 1
    return counter

print(last2('hixxhi'))
print(last2('xaxxaxaxx'))
print(last2('axxxaaxx'))

# My tests
print(last2('axxaxxxxaxx')) # should be 4



