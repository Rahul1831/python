def is_prime(x):
    if x<=1:
        return False
    for i in range(2,int(x**0.5)+1):
         if x % i == 0:
            return False
    return True
num=int(input("Enter your number: "))
print(is_prime(num))