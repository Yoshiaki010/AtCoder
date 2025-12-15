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

pair = []
num_list = [0] * 10

pair = [S[0]]
num_list[S[0]] += 1
serchmode = 0

print(S)
print(pair,num_list)

ans = 0
for i in range(1,N):
    num_list[S[i]] += 1

    if serchmode == 0:
        if pair[0] + 1 == S[i]:
            ans += 1
        else:
            if 1 < len(pair):
                if pair[1] + 1 == S[i]:
                    ans += 1
                    pair = [pair[1],S[i]]
                else:
                    num_list[pair[0]] = 0
                    num_list[pair[1]] = 0
                    pair = [S[i]]
            else:
                num_list[pair[0]] = 0
                pair = [S[i]]

print(ans)

#lv4
"""
print(pow(10,-1,11))
print(pow(100,-1,11))
"""
