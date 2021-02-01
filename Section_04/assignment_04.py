# Assignment 4

"""
Given a non-empty string like "Code" return a string like "CCoCodCode".

grow_string('Code') → 'CCoCodCode'
grow_string('abc') → 'aababc'
grow_string('ab') → 'aab'

"""

# Remember this one.

def grow_string(text):
    result = ''
    # Make sure to get the last symbol
    for letter in range(0, len(text)+1):
        result += text[:letter]
    return result

print(grow_string("HELLOYES"))