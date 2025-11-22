#lv1
"""
X,Y,Z = map(int,input().split())

diff = X - (Y * Z)
if -1 < diff and diff % (Z - 1) == 0:
    ans = "Yes"
else:
    ans = "No"
print(ans)
"""

#lv2
"""
N = int(input())
a = list(map(int,input().split()))

for i in range(N):
    hight = a[i]
    for j in range(i):
        back = i - j - 1
        if hight < a[back]:
            ans = back + 1
            break
        else:
            continue
    else:
        ans = -1
    print(ans)
"""

#lv3
"""
"""
S = list(map(int,list(input())))
N = len(S)

pair = -1
num_list = [0] * 10

pair = S[0]
num_list[S[0]] += 1

print(S)
print(pair,num_list)

ans = 0
for i in range(1,N):
    num_list[S[i]] += 1

    print(pair,num_list,S[i],end = "")
    if pair + 1 == S[i]: 
        print("+",end = "")
        ans += 1
        if num_list[S[i]] == num_list[pair]:
            num_list[pair] = 0
            pair = S[i]
    elif pair == S[i]:
        pass
    else:
        num_list[pair] = 0
        pair = S[i]
    print()
    print(pair,num_list)
    print()

print(ans)