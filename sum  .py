for i in range(100):
    num = int(input("Enter a positive number: "))
    if num > 0:
        break
        print("Invalid! Try again.")
j=0
while num>0:
    k=num%10
    j=j+k

    num=num//10
    
print(j)

print(eval(input("Enter expression (e.g., 2+3*4): ")))