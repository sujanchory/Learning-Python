num=int(input())
temp=num
summ=0
while num>0:
     r=num%10
     num=num//10
     fact=1
     for i in range(r,0,-1):
         fact=fact*i
     summ+=fact
if summ==temp:
    print(temp,'is a Strong Number')
else:
    print(temp,'is not a Strong Number')
