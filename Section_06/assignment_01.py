# Find the words specified in words_to_aggregate in dir_with_files. Find the number of times
# The word appears in the files.
# Expected output: the dictionary with the number of times the word was found total.

import re
import sys
import os

# Using hardcoded values.
# dir_with_files = os.getcwd() + "\\project_files"
# words_to_aggregate = ["hello", "Peter", "computer"]

# Passing it out as a script in cmd.
dir_with_files = sys.argv[1]
words_to_aggregate = sys.argv[2:]
results = {}

for current_dir, dirs, files in os.walk(dir_with_files):
    # We need only the file with the current dir.
    for file in files:
        # For readability.
        print("The matches found in file:", file)
        # Let's open the file in the directory.
        with open(os.path.join(current_dir, file), encoding="utf-8") as f:
            # Now let's check for the words in the file.
            for word in words_to_aggregate:
                # For readability. Also, we use a simple regex expression to find all the matches of a word.
                found_item = re.findall(word, f.read())
                # We get back a list, so we can just find the len of it.
                # Plus additional print statements
                print("The word:", word, "was found:", len(found_item), "times.")
                # Add the word to the dict.
                if word not in results:
                    results[word] = 0
                # If in the dict, just add the len of the list.
                else:
                    results[word] = results[word] + len(found_item)
                # Come back to the start of the file for a second/third word, etc.
                f.seek(0)

# The expected output.
print(results)