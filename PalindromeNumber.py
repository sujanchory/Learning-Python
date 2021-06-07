"""
n=int(input())
a=n
rev=0
while n>0:
   r=n%10
   rev=rev*10+r
   n=n//10
if a==rev:
    print(a,'is a palindrome number')
else:
    print(a,'is not a palindrome number')
"""

n=input()
if n==n[: :-1]:
    print(n,'is a palindrome number')
else:
    print(n,'is not a palindrome number')
 
