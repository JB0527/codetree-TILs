n, m = map(int, input().split())
clothes = [tuple(map(int, input().split())) for _ in range(n)]
s = [x[0] for x in clothes]
e = [x[1] for x in clothes]
v = [x[2] for x in clothes]

dp = [0]*(m+1)
maxv = 0
for tmp in range(n):
    if s[tmp] == 1:
        maxv = max(maxv,v[tmp])
dp[0] = maxv
# 날짜정리

score=[0]*n
for i in range(m):
    # 물자정리
    maxvv = 0
    for j in range(n):
        if s[j]<=i+1<=e[j] :
            maxvv = max(maxvv,abs(dp[i] - v[j]))
            if maxvv == abs(dp[i] - v[j]):
                dp[i+1] = v[j]
ans = 0
for i in range(1,m):
    ans += abs(dp[i]-dp[i-1])
print(ans)