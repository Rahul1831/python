class student:
    def __init__(self,name):
        self.name = name
s = student("rahul")
print(hasattr(s,"name"))
print(type(s))
if hasattr(s,"name"):
    print(getattr(s,"name"))
print(dir(student))
print(id(s))