import math
a,b= map(int,input('Enter Two Numbers: ').split())
#print(math.gcd(a,b))
if a>b:
    a,b=b,a
for i in range(a,0,-1):
    if a%i==0 and b%i==0:
        print("The GCD of",a,b,"is",i)
        break
            
