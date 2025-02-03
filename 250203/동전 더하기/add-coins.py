n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

# Write your code here!
counts = 0
for i in range(n-1,0,-1):
    ans = k // coins[i]
    k -= ans*coins[i]
    counts += ans
if k == 0:
    print(counts)
