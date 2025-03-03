#lv1
""" 
n = int(input())
a = list(map(int,input().split()))
ans = "Unknow"
for i in range(n - 1):
    if a[i] < a[i + 1]:
        ans = "Yes"
    else:
        ans = "No"
        break
print(ans)
"""
#lv2
"""
n = int(input())
ans = [["?" for _ in range(n)] for _ in range(n)]

for i in range(n):
    j = n - i
    if i <= j:
        if i % 2 == 0:
            color = "#"
        else:
            color = "."
        for l in range(j - i):
            for k in range(j - i):
                ans[i + l][i + k] = color
for i in range(n):
    print("".join(ans[i]))
"""
#lv3
"""
n = int(input())
a = list(map(int,input().split()))
numbers = {}
ans = 10 ** 5 * 2 + 1
for i in range(n):
    if a[i] in numbers:
        if i - numbers[a[i]] + 1 < ans:
            ans = i - numbers[a[i]] + 1
    numbers[a[i]] = i
if ans == 10 ** 5 * 2 + 1:
    ans = -1

print(ans)
"""
#lv4
"""
N,Q = map(int,input().split())
bird = [i for i in range(N)]
nest = [i+1 for i in range(N)]
nestdict = {}
for i in range(N):
    nestdict[i+1] = i

for _ in range(Q):
    op = input()
    if op[0] == "1":
        num,a,b = map(int,op.split())
        bird[a-1] = nestdict[b]
    elif op[0] == "2":
        num,a,b = map(int,op.split())
        nest[nestdict[a]] = b
        nest[nestdict[b]] = a
        nestdict_a = nestdict[a]
        nestdict[a] = nestdict[b]
        nestdict[b] = nestdict_a
    else:
        num,a = map(int,op.split())
        print(nest[bird[a-1]])
"""