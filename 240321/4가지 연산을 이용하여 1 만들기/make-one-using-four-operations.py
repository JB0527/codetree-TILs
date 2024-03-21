"""
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
que = deque()
que.append((n,0))
visited = [n]
answer = 0

def bfs():
    global answer
    while que:
        num, time = que.popleft()
        if num == 1:
            answer = time
            return print(answer)

        elif num // 3 not in visited and num % 3 == 0:
            visited.append(num // 3)
            que.append((num//3,time + 1))
                
        elif num // 2 not in visited and num % 2 == 0:
            visited.append(num // 2)
            que.append((num//2,time + 1))
                
        elif num % 2 != 0 and num% 3 != 0:
            if num-1 not in visited and (num-1) % 3 == 0:
                visited.append(num-1)
                que.append((num-1,time + 1)) 
            elif num+1 not in visited and (num+1) % 3 == 0:
                visited.append(num+1)
                que.append((num+1,time + 1))
            elif num-1 not in visited and (num-2) % 3 == 0:
                visited.append(num-1)
                que.append((num-1,time + 1)) 
            elif num-1 not in visited and (num-1) % 2 == 0:
                visited.append(num-1)
                que.append((num-1,time + 1))
bfs()
"""
import sys
input = sys.stdin.readline 
from collections import deque

n = int(input())
que = deque()
que.append((n, 0))
visited = [n]
answer = 0

def bfs():
    global answer
    while que:
        now_num, time= que.popleft()
        if now_num == 1:
            answer = time
            return 

        if now_num//3 not in visited and now_num % 3 == 0:
            visited.append(now_num//3)
            que.append((now_num//3, time+1))
        if now_num//2 not in visited and now_num % 2 == 0:
            visited.append(now_num//2)
            que.append((now_num//2, time+1))
        if now_num-1 not in visited:
            visited.append(now_num-1)
            que.append((now_num-1, time+1))
        if now_num+1 not in visited:
            visited.append(now_num+1)
            que.append((now_num+1, time+1))

bfs()
print(answer)