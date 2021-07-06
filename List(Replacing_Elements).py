nums=list(map(int,input().split()))
index=list(map(int,input().split()))
l=list()
for i in range(len(nums)):
    l.insert(index[i],nums[i])
print(l)
    
