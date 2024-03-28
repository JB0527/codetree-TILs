s = str(input())
p = str(input())

len_s =len(s)
len_p = len(p)
#dp = [[0 for _ in range(len_s + 1)] for _ in range(len_p+1)]

#dp[0][0] = 1


for j in s:
    for l,k in enumerate(p):
        if k == '.':
            continue
        elif j == k:
            real = l
        else:
            real = 0

for i, tmp in enumerate(p[real:]):
    for j in s:
        if j != tmp:
            if tmp == '*':
                if p[real+i-1] == j:
                    continue
            elif tmp == '.':
                continue
            else:
                answer = 'false'
                break
        elif j == tmp:
            continue
    if answer == 'false':
        print('false')
        break
    else:
        print('true')
        break