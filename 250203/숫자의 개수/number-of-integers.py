n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [int(input()) for _ in range(m)]

# Write your code here!
def lower_bound(i):
    left = 0
    right =n-1
    min_idx = n
    while left <= right:
        mid = (left+right) // 2
        if arr[mid] >= i:
            min_idx = min(min_idx,mid)
            right = mid - 1
        else:
            left = mid+1
    return min_idx
def upper_bound(i):
    left = 0
    right =n-1
    min_idx = n
    while left <= right:
        mid = (left+right) // 2
        if arr[mid] > i:
            min_idx = min(min_idx,mid)
            right = mid - 1
        else:
            left = mid+1
    return min_idx

for i in queries:
    ans = upper_bound(i) - lower_bound(i)
    print(ans)