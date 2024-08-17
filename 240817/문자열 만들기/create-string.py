def make_lexicographically_smallest_string(n, S):
    left, right = 0, n - 1
    T = []
    
    while left <= right:
        if S[left] < S[right]:
            T.append(S[left])
            left += 1
        elif S[left] > S[right]:
            T.append(S[right])
            right -= 1
        else:
            l, r = left, right
            while l < r and S[l] == S[r]:
                l += 1
                r -= 1
            if S[l] < S[r]:
                T.append(S[left])
                left += 1
            else:
                T.append(S[right])
                right -= 1
    
    return ''.join(T)

# 입력
n = int(input())
S = input()

# 결과 출력
print(make_lexicographically_smallest_string(n, S))