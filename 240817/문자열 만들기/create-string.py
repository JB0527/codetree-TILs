n = int(input())
s = list(str(input()))
T = []
def check():
    if s[0] < s[-1]:
        T.append(s[0])
        s.remove(s[0])
        #print(s)
    else:
        T.append(s[-1])
        s.pop()
        #print(s)


for i in range(n):
    if s[0] != s[-1]:
        check()
    else:
        check()
print("".join(T))