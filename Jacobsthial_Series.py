'''Jacobsthal Number'''
n=int(input('Enter Raange: '))
a=0
b=1
print(a,b,end=' ')
for i in range(3,n+1):
    c=2*a+b
    a=b
    b=c
    print(c,end=' ')
