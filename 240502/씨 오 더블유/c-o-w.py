n = int(input())
cow = list(input())
#print(cow)
c = 0
o = 0
w = 0
for i in cow:
    if i == 'C':
        c+=1
    elif i == 'O':
        o+=1
    elif i == 'W':
        w+=1

print(c*o*w)