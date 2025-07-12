class car:
    def __init__(self , brand,year):
        self.brand= brand
        self.year=year
c=car("bmw","2004")
b=car("benz","2006")
print(b.brand,b.year)
print(c.brand,c.year)