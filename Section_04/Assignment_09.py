# Assignment 9

"""
We have 2 variables. fr and d. fr is a list of strings and d is a dictionary with email
addresses as keys and numbers as values (numbers in string format).
Write code to replace the email address in each of the strings in the fr list with
the associated value of that email looked up from the dictionary d.
If the dictionary does not contain the email found in the list, add a new entry
in the dictionary for the email found in the fr list. The value for this new email key
will be the next highest value number in the dictionary in string format.

Once the dictionary is populated with this new email key and a new number value,
replace that email's occurrence in the fr list with the number value.

The output of running your completed code should be the following:

Value of fr:
['199|4|11|GDSPV', '199|16|82|GDSPV', '205|12|82|GDSPV', '206|19|82|GDSPV']
Value of d:
{'7@comp1.COM': '199', '8@comp4.COM': '200', '13@comp1.COM': '205', '26@comp1.COM': '206'}

"""

# Don't manually change fr and d.
fr = ['7@comp1.COM|4|11|GDSPV', '7@comp1.COM|16|82|GDSPV', '13@comp1.COM|12|82|GDSPV',
      '26@comp1.COM|19|82|GDSPV']

d= {'7@comp1.COM': '199', '8@comp4.COM': '200', '13@comp1.COM': '205'}

fr_split = []

# Let's split the items in fr.
for item in fr:
    fr_split.append(item.split('|'))

# Get and check the emails in d.
for email in fr_split:
    # email is the first item in the list so: email[0]
    # Let's start by checking if there are any mismatches:
    if email[0] not in d:
        max_value = int(max(d.values()))
        d[email[0]] = str(max_value + 1)
    # If there's an email:
    if email[0] in d:
        email[0] = d[email[0]]

# Now all that's left is to correct fr and we're done.
fr = []
for item in fr_split:
    fr.append('|'.join(item))

# don't change the below:
# --------------------------------------
print("Value of fr: ")
print(fr)
print("Value of d:")
print(d)


# Will also check the other solutions.
