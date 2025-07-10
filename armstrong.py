def armstrong(n):
    a=n
    b=n
    count=0
    while a!=0:
         a=a//10
         count+=1
    sum=0
    while b!=0:
        x = b%10
        sum+=x**count
        b= b//10
    if n == sum:
        print(f'{n} is a armstrong number')

for i in range(1,1000):
    armstrong(i)
