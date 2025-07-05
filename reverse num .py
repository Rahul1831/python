i= int(input())
j= 0
k= 0

while i>0:
    k= i%10
    j= j*10+k
    
    i=i//10
print(j)