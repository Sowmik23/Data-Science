import re
text = "This course will introduce the basics of data science"
match = re.search(r"data science", text)
print(match.start()) #print the start index where match the text


match = re.match(r"data science", text) # check if start of text matches
match = re.search(r"data science", text) # find first match or None
for match in re.finditer("data science", text):
# iterate over all matches in the text
...
all_matches = re.findall(r"data science", text) # return all matches