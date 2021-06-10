n=int(input('Enter Raange: '))
a=0
b=1
c=1
print(a,b,c,end=' ')
for i in range(4,n+1):
    d=a+b+c
    a=b
    b=c
    c=d
    print(d,end=' ')
