import itertools
"""n = int(input())
info = [list(map(int,input().split())) for _ in range(n)]
chars = []
for i in range(n):
    chars.append(i)
order = itertools.permutations(chars, 2)
answer = 0

for i,j in order:
    if not info[i][j] == 0:
        answer += info[i][j]
print(answer)
"""
import itertools
#외판원순열에 1로돌아가는거까지 추가
def calculate_cost(path, info):
    cost = 0
    n = len(path)
    for i in range(n - 1):
        if info[path[i]][path[i + 1]] == 0:
            continue
        cost += info[path[i]][path[i + 1]]
    cost += info[path[-1]][path[0]]  
    return cost

n = int(input())
info = [list(map(int, input().split())) for _ in range(n)]
chars = list(range(n))
min_cost = float('inf')

for path in itertools.permutations(chars):
    cost = calculate_cost(path, info)
    min_cost = min(min_cost, cost)

print(min_cost)