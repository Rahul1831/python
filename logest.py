from functools import reduce
words = ["cat", "lion", "elephant", "dog"]
result = reduce(lambda x, y: x if len(x) > len(y) else y, words)
print(result)