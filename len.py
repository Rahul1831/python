class rectangle:
    def __init__(self ,length,width):
        self.length= length
        self.width=width
    def area(self):
        return self.length* self.width
a=rectangle(5,6)
print(a.area())