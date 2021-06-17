def prime(n):
    for i in range (2,n):
     if n%i==0:
        return False
     else:
        return True

def mp(n):
   if prime(n):
      while n:
        rem=n%10
        if prime(rem)==False:
            return False
        n=n//10
      else:
       return True
   else:
        return False

n= int(input())
print(mp(n))
