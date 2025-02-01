#lv1
"""
a,b=map(int,input().split())
print((a+b)**2)
"""
#lv2
"""
x = int(input())
table=[]
for i in range(9):
    block = []
    for j in range(9):
        block.append((i+1)*(j+1))
    table.append(block)

ans=0
for i in range(9):
    for j in range(9):
        if table[i][j] != x:
            ans += table[i][j]
        else:
            continue
print(ans)
"""
#lv3
"""
"""
l,r=input().split()

#上限から上限の-1までの通りを計算する関数
def uprange(u,k,t):
    print(-k,int(r[-k]),end=":")
    if u < int(r[-k]):
        t = u + 1
    else:
        t = int(r[-k]) + 1
    print(t)
    if k == 1:
        return t
    else:
        return t * uprange(u,k-1,t)

#下限側の通り計算関数
#def lowrange(u,k,t):


ans = 0
ans += uprange(8,3,1)
print(ans)
# 上限の-1から下限までの間の通りの計算
ans += int(r[0]) ** (len(r)-1)
print(int(r[0]) ** (len(r)-1))
#ans += lowrange(,,)
print(ans)

