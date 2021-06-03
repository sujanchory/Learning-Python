def mul(a,b):
 summ=0
 while a!=0:
    if a%2:
      summ+=b  
    a=a//2
    b=b*2
 return summ

a,b=map(int,input().split())
summ=mul(a,b)
print(summ)
       
