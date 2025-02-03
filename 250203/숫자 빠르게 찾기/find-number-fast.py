n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [int(input()) for _ in range(m)]

# Write your code here!
queries

for i in range(m):
    left = 0
    right = n-1
    ans = 0
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == queries[i]:
            print(mid+1)
            ans = 'good'
            break
        
        if arr[mid] > queries[i]:
            right = mid -1
        else:
            left = mid + 1
    if ans == 0:
        print(-1)