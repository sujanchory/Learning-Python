def fact(n):
    if n==1 or n==0:
        return 1
    else:
       return(n*fact(n-1))
n=int(input())
print(fact(n))

##def fact(n):
##    f=1
##    for i in range(1,n+1):
##        f*=i
##    return f
##f=int(input())
##print(fact(f))
