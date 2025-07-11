from functools import reduce
list=[1,3,5,6]
total= reduce(lambda x ,y:x*y , list  )
print(total)