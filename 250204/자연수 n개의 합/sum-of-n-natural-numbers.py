import math
s = int(input())
# Write your code here!
left = 1 
right = int(math.sqrt(s*2))
min_num = s+1
while left <= right:
    mid = (left+right)//2
    if mid * (mid+1)//2 > s:
        right = mid - 1
        min_num = min(min_num,mid)
    else:
        left = mid +1

print(mid-1)