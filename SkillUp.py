##a=100
##b=20
##if (a<b):
##    print(a+b)
##else:
##    print(a-b)
##    
##print('done')


##a=int(input())#10
##b=int(input())#10
##
##if a>b:
##    print(a,"is bigger")
##elif a==b:
##    print(a,b,'are same')
##else:
##    print('number',b,'is bigger')


##a=int(input())#10
##b=float(input())#20
##c=input()

##per=int(input())
##bl=int(input())
###>=60,no backlogs
##if per>=60 and bl==0:
##    print('eligible')
##else:
##    print('not eligible')


##m=int(input())
##
##if m>=0 and m<=100:
##    if m>=80:
##        print('A grade')
##    elif m>=60 and m<80:
##        print('B grade')
##    elif m>=40 and m<60:
##        print('C grade')
##    else:
##        print('Failed')
##
##else:
##    print('Invalid marks')


##m=35
##if m>=80:
##    print('A')
##elif 80>m>=60:
##    print('B')
##elif 60>m>=40:
##    print('C')
##else:
##    print('failed')


##uid=input()
##upw=input()
##
##if uid=='thub@123.com' and upw=='python123':
##    print('login successfully')
##else:
##    print('wrong credintials')


##uid=input()
##upw=input()
##
##if uid=='thub@123.com' :
##    if upw=='python123':
##        print(' "login successfully" ')
##    else:
##        print('wrong password')
##else:
##    print('wrong id')
    

##for i in range(1,10):#1,2,3,4,5,6,7,8,9
##    print(i,end=' ')#1,2,3,4,5,6,7,8,9

##for i in range(1,11,1):#1,2
##    print(i,end=' ')#1
##    i+=2#3
##    print(i)#3

##for i in range(1,11,3):
##    print(i,end=' ')

##for i in range(1,11,1):
##    print(i,end=' ')
##
##print()
##print(i)
##
##
##print()

##i=1#1
##while i<=10:#1,2,3,4,5,6,7,8,9,10
##    print(i,end=' ')#1,2,3,4,5,6,7,8,9,10
##    i+=1#2,3,4,5,6,7,8,9,10,11

##i=-10
##while i<=1:
##    print(i,end=' ')
##    i+=2

##i=1
##while i<10:
##    print(i,end=' ')


##for i in range(1,11):
##    print(i,end=' ')
##    if i==5:
##        
##        break
##print('done')
##
##
##for i in range(1,11):
##    if i==5:
##        continue
##    print(i,end=' ')
##
##print('done')

##i=1
##while i<=10:
##    if i==6:
##        break
##    print(i,end=" ")
##    i+=1
##
##print('done')


##i=0
##while i<10:
##    i+=1
##    if i==5:
##        continue
##    print(i,end=" ")
##print('done')

##for i in range(1,11):
##    if i==5:
##        break
##    print(i,end=' ')
##else:
##    print('done')


##for i in range(1,11,1):#1,3
##    print(i,end=' ')#1
##    i+=2#3
##    
##    print(i)#3
##    


##for i in range(1,10,2):
##    print(i,end=' ')
##
##print()
##
##for i in range(1,10):
##    if i%2==1:
##        print(i,end=' ')
##
##print()
##
##for i in range(1,10):
##    if i%2==0:
##        continue
##    print(i,end=' ')

##n=int(input('enter a number: '))
##s=int(input('enter a start point: '))
##e=int(input('enter end point: '))
##
##for i in range(s,e+1):
##    print(n,'*',i,'=',n*i)
##
##while s<=e:
##    print(n,'*',s,'=',n*s)
##    s+=1

##n = int(input("Number: "))
##j = int(input("End Value:"))
## 
##i = 1
##while i <= j:
##    n * i
##    print(f"{n} * {i} = {n * i}"))
##    i += 1



##n=int(input('enter a number: '))#5
##s=int(input('enter a start point: '))#6
##e=int(input('enter end point: '))#3
##
##if s<e:#6<3 false
##    for i in range(s,e+1):
##        print(n,'*',i,'=',n*i)
##else:        
##    for i in range(s,e-1,-1):#(6,5,4,3)
##        print(n,'*',i,'=',n*i)


##s=int(input('enter a start point: '))#10
##e=int(input('enter end point: '))#25
##n=int(input('enter a number'))#3
##for i in range(s,e+1):
##    if i%n==0:
##        print(i,end=' ')


##n=int(input('enter a number: '))#5
##c=0
##for i in range(1,n+1):#1,2,3,4,5
##    if n%i==0:#1,5
##        c+=1#1,2
##        print(i)
##
##if c==2:
##    print(n,'is prime')
##else:
##    print(n,'is not a prime')

##n=int(input('enter a number: '))#9
##for i in range(2,n):#(2,9)  2 3 4 5 6 7 8
##    if n%i==0:#3
##        print(n,'is not a prime')
##        break
##else:
##    print(n,'is a prime')

##n=int(input('enter a number: '))
##c=0
##for i in range(1,(n//2)+1):
##    if n%i==0:
##        c+=1
##if c>1:
##    print(n,'is not a prime')
##else:
##    print(n,'is a prime')

##n=int(input('enter a number: '))
##import math
##s=int(math.sqrt(n))
##
##c=0
##
##for i in range(1,s+1):
##    if n%i==0:
##        c+=1
##
##if c>1:
##    print(n,'is not a prime')
##else:
##    print(n,'is a prime')

      
##n=int(input('enter a number: '))#253
##a=n
##rev=0
##while n:#253,25,2
##    rem=n%10#
##    rev=rev*10+rem
##    n=n//10   
##print(rev)
##
##if rev==a:
##    print(a,'is a palindrome')
##else:
##    print(a,'is not a palindrome')


##n=input('enter a number: ')
##if n==n[::-1]:
##    print(n,'is a palindrome')
##else:
##    print(n,'is not a palindrome')


##n=int(input('enter series range: '))
##a=0
##b=1
##print(a,b,end=' ')
##for i in range(3,n+1):
##    c=a+b
##    a=b
##    b=c
##    print(b,end=' ')

##n=int(input('enter series range: '))
##a=0
##b=1
##print(a,b,end=' ')
##for i in range(3,n+1):
##    c=2*a+b
##    a=b
##    b=c
##    print(b,end=' ')


##n=int(input('enter series range: '))
##a=0
##b=0
##c=1
##print(a,b,c,end=' ')
##for i in range(3,n+1):
##    d=a+b+c
##    a=b
##    b=c
##    c=d
##    print(c,end=' ')

##a=int(input())#3
##b=int(input())#10
##if a>b:#
##    a,b=b,a
##c=b#10
##while True:
##    if c%a==0 and c%b==0:#10,11,12,13.....30
##        print('LCM of',a,b,'is',c)
##        break
##    c+=1


##a=int(input())#8    12 
##b=int(input())#12   8
##if a>b:#12>8
##    a,b=b,a#8 12
##print(a,b)
##for i in range(a,0,-1):#8,7,6,5,4
##    if a%i==0 and b%i==0:#4
##        print('gcd of',a,b,'is',i)
##        break
##    


##def example():
##    print(10+20)
##
##example()


##def example(a,b):#formal parameters
##    print(a+b)
##
##x=int(input('enter a number: '))
##y=int(input('enter a number: '))
##example(x,y)#actual parameters
##
##n=int(input('enter a number: '))
##m=int(input('enter a number: '))
##example(n,m)#actual parameters


##def example(c,d):#formal parameters
##    print(c+d)#9
##x=int(input('enter a number: '))#4
##y=int(input('enter a number: '))#5
##example(x,y)#actual parameters
##
##
##def example(c,d):
##    return(c+d)
##x=int(input('enter a number: '))#4
##y=int(input('enter a number: '))#5
##
##print(example(x,y))#9

##def example():
##    global a
##    a=12#local variable
##    print('inside function',a)
##
##a=10#global variable
##print('before function',a)
##
##example()
##
##a+=1
##print('after function',a)


##def example():
##    global b
##    b=12
##    print('inside function',b)
##
##example()
##
##print('after function',b)



##def prime(n):
##    for i in range(2,n):
##        if n%i==0:
##            #print(n,'is not a prime')
##            break
##    else:
##        print(n,'is a prime')
##
##
##s=int(input('enter a number: '))
##e=int(input('enter a number: '))
##for i in range(s,e+1):
##    prime(i)

##def add(a,b):
##    return(a+b)
##def sub(a,b):
##    return(a-b)
##def mul(a,b):
##    return(a*b)
##def div(a,b):
##    return(a%b)    
##
##a=int(input('enter a number: '))#10
##b=int(input('enter a number: '))#5
##print('1:addition,2:subtraction,3:multiplication,4:division')
##c=int(input('enter a choice: '))
##
##if c==1:
##    add(a,b)
##elif c==2:
##    sub(a,b)
##elif c==3:
##    mul(a,b)
##elif c==4:
##    div(a,b)
##else:
##    print('wrong choice')



##def add(a,b):
##    print(a+b)#huigfushGDFUHSGKFZGf
##add(5,4)
##
##def add1(a,b):
##    return(a+b)
##print(add1(5,4))#kjdsghugsUVGUyg
##

##
##def prime(n):
##    for i in range(2,n):
##        if n%i==0:
##            print('False')
##            break
##    else:
##        print(True)
##
##prime(6)
##


##def prime(n):
##    for i in range(2,n):
##        if n%i==0:
##            return False
##    else:
##        return True

##a=int(input('entera number: '))
##if prime(a):
##    print(a,'is prime')
##    
##while True:
##    a+=1
##    if prime(a):
##        print(a,'is prime')
##        break
        
##def fact(n):#6
##    if n==1 or n==0:
##        return 1
##    else:
##        return(n*fact(n-1))
##print(fact(6))


##def fact(n):
##    f=1
##    for i in range(1,n+1):#1 2 3 4 5 6
##        f*=i#1 1*2  1*2*3 1*2*3*4 1*2*3*4*5 1*2*3*4*5*6
##    print(f)
##fact(6)

##def fact(n):
##    f=1
##    for i in range(1,n+1):#1 2 3 4 5 6
##        f*=i#1 1*2  1*2*3 1*2*3*4 1*2*3*4*5 1*2*3*4*5*6
##    return(f)
##print(fact(6))


##
##def fun(a):
##    c=0
##    for i in a:#python
##        c+=1#123456
##    return(c)
##print(fun('python class'))
##

##def st(a):#python
##    if a is '':
##        return 0
##    else:
##        return(1+st(a[1: ]))
##
##n=input()
##print(st(n))


##def ex():
##    return 
##print(ex())

##def prime(n):
##    for i in range(2,n):
##        if n%i==0:
##            return False
##    else:
##        return True
## 
##def rev(n):
##    a=n
##    r=0
##    while n:#253,25,2
##        rem=n%10#
##        r=r*10+rem
##        n=n//10   
##    return(r)
##
##n=int(input())
##if prime(n) and prime(rev(n)):
##    print(True)
##else:
##    print(False)


##
##def prime(n):
##    for i in range(2,n):
##        if n%i==0:
##            return False
##    else:
##        return True
## 
##def mp(n):
##    if prime(n):
##        while n:
##            rem=n%10
##            if prime(rem)==False:
##                return False
##            n=n//10
##        else:
##            return True
##    else:
##        return False
##
##print(mp(373))



##n=int(input())#4
##for i in range(1,n+1):#rows(1,2,3,4)  1
##    for j in range(1,n+1):#columns  {1:1,2,3,4   2:1,2,3,4  3:1,2,3,4  4:1,2,3,4}
##        print('*',end=' ')
##    print()


##n=int(input())#4
##for i in range(1,n+1):#rows(1,2,3,4)  1 2 3 4
##    for j in range(1,i+1):#columns  {1:1  2:1,2 3:1,2,3  4:1,2,3,4}
##        print('*',end=' ')
##    print()


##n=int(input())#4
##for i in range(1,n+1):
##    for j in range(n,i-1,-1):
##        print('*',end=' ')
##    print()
##
##for i in range(n,0,-1):
##    for j in range(1,i+1):
##        print('*',end=' ')
##    print()


##n=int(input())#
##if n%2==1:
##    for i in range(1,n+1):
##        for j in range(1,n+1):
##            if i==n//2+1 or j==n//2+1:
##                print('*',end=' ')
##            else:
##                print(' ',end=' ')
##        print()
##
##else:
##    print('wrong input')


##n=int(input())
##for i in range(1,n+1):
##    for j in range(1,n+1):
##        if i==1 or i==n or j==1 or j==n:
##            print('*',end=' ')
##        else:
##            print(' ',end=' ')
##    print()

##n=int(input())
##for i in range(1,n+1):
##    for j in range(1,n+1):
##        if i==1 or i==n or j==1 or j==n or i==n//2+1 or j==n//2+1:
##            print('*',end=' ')
##        else:
##            print(' ',end=' ')
##    print()


##for i in range(1,n+1):#rows
##    for k in range(1,n-i+1):#spaces in column
##        print(' ',end=' ')
##    for j in range(1,i+1):# * in columns
##        print('*',end=' ')
##    print()
##
##for i in range(n,0,-1):
##    for j in range(1,n+1):
##        if j>=i:
##            print("*",end=" ")
##        else:
##            print(" ",end=" ")
##    print()

##
##for i in range(1,n+1):
##    for k in range(i,n):
##        print(' ',end=' ')
##    for j in range(1,n+1):
##        if i==1 or i==n or j==1 or j==n:
##            print('*',end=' ')
##        else:
##            print(' ',end=' ')
##    print()

##n=int(input())
##rem=0
##s=''
##while True:
##    rem=n%2
##    print(rem)
##    s+=str(rem)
##    n=n//2
##    if n<=1:
##        print(1)
##        s+=str(1)
##        break
##if len(s)<4:
##    print(0)
##else:
##    print('4th bit',s[3])
##
##n=int(input())
##n=bin(n)
##print('binary',n)
##n=n[2:]
##print('proper binary',n)
##
##n=n[::-1]
##print('reversed',n)
##if len(n)<4:
##    print(0)
##else:
##    print(n[3])

##n=int(input())
##f=int(input())
##c=0
##def fact(n,f,c):
##    for i in range(1,n//2+1):
##        if n%i==0:
##            c+=1
##            if c==f:
##                return i
##    else:
##        return 0
##print(fact(n,f,c))

##n=int(input())
##f=int(input())
##c=0
##i=1
##def fact(n,f,c,i):
##    if i>n:
##        return 0
##    if n%i==0:
##        c+=1
##        if c==f:
##            return i
##        else:
##            return fact(n,f,c,i+1)
##    else:
##        return fact(n,f,c,i+1)
##
##print(fact(n,f,c,i))


##def cp(n):
##    if n==1 or n==3 or n==5 or n==7 or n==2:
##        return 0
##    elif n==8:
##        return 2
##    else:
##        return 1
##
##def cpsum(t):#630
##    s=0
##    while t:#630,63 ,6       
##        rem=t%10#0,3,6
##        t=t//10#63,6,0
##        s+=cp(rem)#s=s+cp(rem)=0+1=1+cp(3)=1+0=1+cp(6)=1+1=2
##    return s        
##t=int(input())
##print(cpsum(t))

##n=int(input())
##
##for i in range(1,n+1):
##    for j in range(1,i+1):
##        print(chr(64+j),end=' ')
##    print()
##

##for i in range(65,65+n):
##    for j in range(65,i+1):
##        print(chr(j),end=" ")
##    print()

##n=int(input())#5
##for i in range(n,0,-1):#5 4 3 2 1
##    for j in range(1,i+1):#5:12345 4:1234
##        print(chr(64+j),end=' ')
##    print()

##n=list(map(int,input().split()))#[4,3,2,1,6,7]

##for i in range(0,len(n)):#(0,6)--0,1,2,3,4,5
##    print(i,n[i])
##
##for i in n:
##    print(i)

##a=list(map(int,input().split()))#[4,5,6,7]
##s=0
##for i in range(0,len(a)):#(0,4) 0,1,2,3
##    s+=a[i]#0+4=4, 4+5=9 9+6=15 15+7=22
##
##print(s)
##
##s=0
##for i in a:
##    s+=i
##print(s)


##a=list(map(int,input().split()))#[3,6,4,1,3]
##cnt=0
##for i in a:#3 6 4 1 3
##    cnt+=1#1 2 3 4 5
##print(cnt)


##a=list(map(int,input().split()))#[2, 7, 8, 9, 7, 5]
####a.sort()
####print(a[-1])
##m=0
##for i in a:
##    if i>m:
##        m=i
##print(m)
##
##
##m=a[0]
##for i in a:
##    if i<m:
##        m=i
##print(m)

##a=list(map(int,input().split()))
##for i in range(0,len(a)):
##    for j in range(i,len(a)):
##        if a[i]>a[j]:
##            a[i],a[j]=a[j],a[i]
##print(a)

##a=list(map(int,input().split()))
##es=0
##os=0
##for i in a:
##    if i%2==0:
##        es+=i
##    else:
##        os+=i
##print(es,os)

##a=list(map(int,input().split()))
##es=0
##os=0
##for i in range(0,len(a)):
##    if i%2==0:
##        es+=a[i]
##    else:
##        os+=a[i]
##print(es,os)


##a=list(map(int,input().split()))
##cnt=0
##for i in range(0,len(a)):
##    for j in range(i,len(a)):
##        if a[i]==a[j] and i<j:
##            print(i,j)
##            cnt+=1
##print(cnt)

##candies=list(map(int,input().split()))
##ec=int(input())
##a=[]
##for i in candies:
##    if i+ec >= max(candies):
##        a.append(True)
##    else:
##        a.append(False)
##print(a)

##nums=list(map(int,input().split()))#[1,2,3,4]
##l=[]
##for i in range(0,len(nums),2):#(0,4,2) i=[0,2]
##    for j in range(nums[i]):#0:1 2:0,1,2
##        l.append(nums[i+1])#[2] [2,4,4,4]
##print(l)
##    
##
##nums=list(map(int,input().split()))#[1,2,3,4]
##l=[]
##for i in range(0,len(nums),2):#(0,4,2)  i=0,2
##    a=[nums[i+1]]*nums[i]#[nums[1]]*nums[0]=[2]*1=[2]
###                      ##[nums[3]]*nums[2]=[4]*3=[4,4,4]
##    l.extend(a)#[2],[2,4,4,4]
##print(l)


##start=int(input())#0
##n=int(input())#5
##xr=0
##for i in range(start,start+n*2,2):#(0,10,2) 0 2 4 6 8   
##    xr=xr^i#0 2 6 0 8
##    print('list',i,'xor',xr)
##print("xr=",xr)



##nums=list(map(int,input().split()))
##index=list(map(int,input().split()))
##t=[]
##for i in range(0,len(index)):
##    t.insert(index[i],nums[i])
##print(t)

##p=list(map(int,input().split()))#
##d=[]
##for i in range(len(p)):
##    for j in range(i+1,len(p)):
##        if p[i]>=p[j]:
##            d.append(p[i]-p[j])
##            break
##    else:
##        d.append(p[i])
##print(d)

##
##prices=list(map(int,input().split()))
##i=0
##j=0
##def solution(prices,i,j):
##    t=prices[i+1:]
##    if i>len(prices)-1:
##        return prices
##    
##    if j>=len(t):
##        solution(prices,i+1,j=0)
##    elif t[j]<prices[i]:
##        prices[i]-=t[j]
##        solution(prices,i+1,j=0)
##    else:
##        solution(prices,i,j+1)
##solution(prices,i,j)
##print(prices)


##h=list(map(int,input().split()))
##s=h.copy()
##h.sort()
##c=0
##for i in range(len(h)):
##    if h[i]!=s[i]:
##        c+=1
##print(c)

##n=list(map(int,input().split()))
##l=len(n)
##def arr(n):
##    for i in range(len(n)-1,-1,-1):
##        if n[i]==0:
##            n.insert(i+1,0)
##        if len(n)>l:
##            n.pop()
##arr(n)
##print(n)


##n=tuple(map(int,input().split()))#3 4 2 6
##
##for i in n:
##    print(i)
##
##for i in range(len(n)):
##    print(i,n[i])

##n=set(map(int,input().split()))#3 4 2 6
##for i in n:
##    print(i)

##a=list(map(int,input().split()))#3 4 5 6
##b=list(map(int,input().split()))#6 7
##for i in b:#6 7
##    if i not in a:#7
##        a.append(i)
##print(a)
    

##a={1:10,2:20,3:30}
##
##for i in a.keys():
##    print(i,a[i])
##
##for i in a.values():
##    print(i)
##
##for i,j in a.items():
##    print(i,j)

##a={}
##n=int(input('enter number of students:'))#3
##for i in range(n):#0 1
##        x=input('enter student name')#s1
##        y=list(map(int,input().split()))#[23,34]
##        a[x]=y#{'s1':[23,34]}
##print(a)

##a={}
##n=int(input('enter number of students:'))#3
##for i in range(n):#0 1
##        x=input('enter student name')#s1
##        y=list(map(int,input().split()))#[23,34]
##        a[x]=y#{'s1':[23,34]}
##print(a)
##b=[]
##
##for i in a.keys():
##    b.append(sum(a[i])/len(a[i]))
    


import random
s=set()
while len(s)<=20:
        s.add(random.randint(1,100))
l=list(s)
print('list is:',l)
print('average is:',sum(l)/len(l))
print('maximum,minimum are:',max(l),min(l))
l=sorted(l)
print('second maximum,second minimum are:',l[1],l[-2])
ec=0
for i in l:
        if i%2==0:
                ec+=1
print('even count is:',ec)


















