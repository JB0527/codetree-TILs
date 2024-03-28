'''
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
answer = []
for i, tmp in enumerate(p[real:]):
    for j in s:
        if j != tmp:
            if tmp == '*':
                if p[real+i-1] == j:
                    continue
            elif tmp == '.':
                continue
            else:
                answer.append(j)
                break
        elif j == tmp:
            continue
    if answer == 'false':
        print('false')
        break
    else:
        print('true')
        break
'''
s = input()
p = input()

len_s = len(s)
len_p = len(p)

# Initialize a 2D DP table
dp = [[False] * (len_p + 1) for _ in range(len_s + 1)]

# Base case: empty string and empty pattern match
dp[0][0] = True

# Handle cases where '*' in the pattern can match an empty sequence
for j in range(2, len_p + 1):
    if p[j - 1] == '*':
        dp[0][j] = dp[0][j - 2]

for i in range(1, len_s + 1):
    for j in range(1, len_p + 1):
        if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
            dp[i][j] = dp[i - 1][j - 1]
        elif p[j - 1] == '*':
            dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))

# Check if the last cell of the DP table is True
if dp[len_s][len_p]:
    print('true')
else:
    print('false')