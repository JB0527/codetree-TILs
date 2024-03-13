K, N = list(map(int, input().split()))

ans = []

def choose(n):
    if n == 0:
        for elem in ans:
            print(elem, end=' ')
        print()
        return
    for k in range(1, K+1):
        ans.append(k)
        choose(n-1)
        ans.pop()
    return

choose(N)