"""
Re module in python
    1.

"""
import re
# Examples:

# ^S.+a
# S[a-t]*$
#
#
# ^ - matches start of the string
# $ - matches end of the string
# \d - numerical digits
# \D - non-numerical
# \s - matches whitespace
# \S - matches any non-whitespace char
# \w - matches a-z, A-Z, 0-9 and _
# \W - matches opp of \w
#
# Quantifiers:
# * - 0 or more
# ? - 0 or 1
# + - 1 or more
# {n} - exactly n occurences

# Example-1
names = ["Finn Bindeballe",
         "Geir Anders Berge",
         "HappyCodingRobot",
         "Ron Cromberge",
         "Sohil"
         ]
ppl_with_first_last_name = []
for name in names:
    result = re.search(r'^\w+\s+\w+$',name)
    if result:
        ppl_with_first_last_name.append(name)
print(ppl_with_first_last_name)
"""
    Output:
        ['Finn Bindeballe', 'Ron Cromberge']
"""

# Example-2
# Search for word char sequence starting with C
print(names)
for name in names:
    result1 = re.search(r'C\w*', name)
    if result1:
        print(name)
        print(result1.group())
        print(result1.span())
        print(result1.start())
        print(result1.end())
"""
    Output:
        HappyCodingRobot
        CodingRobot
        (5, 16)
        5
        16
        Ron Cromberge
        Cromberge
        (4, 13)
        4
        13
"""

# Example - 3
names2 = [
    "Brian Daugette",
    "Veronica Supersonica",
    "Tony Gasparovic",
    "Patrick Germann",
    "m!sha"
]
print(names2)
for name in names2:
    search_res = re.search(r'(\w+)\s+(\w+)', name)
    if search_res:
        print(name)
        print(search_res.group(1))
        print(search_res.group(2))


for name in names2:
    regex = "[a-z]+"
    matches = re.findall(regex, name)
    if matches:
        print(matches)

# To get access
for name in names2:
    regex = "[a-z]+"
    matches = re.finditer(regex, name)
    for match in matches:
        print(match)

# OTher functions
# match function: searches onnly from the beginning
values = [
    "https://www.socratica.com",
    "http://www.socratica.org",
    "file://test.this.path",
    "com.socratic.www_https://"
]
regex = "https?"
for value in values:
    if re.match(regex, value):
        print(value)
    # print(res)

# fullmatch function
regex = "https?://w{3}.\w+.(com|org)"
for value in values:
    if re.fullmatch(regex, value):
        print(value)

# Other functions:
# 1. split function
# 2. sub function
# reference: https://docs.python.org/3/library/re.html