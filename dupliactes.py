def dup():
    li=[]
    x=0
    n=int(input("Enter size of list: "))
    for i in range(n):
        x=int(input(f"Enter element no {i+1}: "))
        li.append(x)
    li=list(set(li))
    return li
print(dup())

    
    

    


    