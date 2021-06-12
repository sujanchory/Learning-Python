def prime(n):
    for i in range(2,n):
        if n%i==0:
            break
    else:
        print(n)
s,e=map(int,input('Enter Starting and ending Ranges: '.split())
for i in range(s,e+1):
        prime(i)
                
                
