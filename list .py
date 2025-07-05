try:
    list=[10,20,30,40,50]
    i=int(input())
    print(list[i])
except IndexError:
    print("its not valid try other index")
except ValueError: 
    print("enter int values")


