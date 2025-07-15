import re
x = "I have 3 apples and 12 bananas"
y = re.findall("\d+",x)
print(y)