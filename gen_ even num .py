def even():
    for i in range(10,31):
        if i%2==0:
            yield i
print(list(even()))           

    