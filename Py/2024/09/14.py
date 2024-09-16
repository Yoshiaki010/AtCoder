# lv1
"""
s=input().split()
a=0
b=0
c=0
if s[0] == "<":
    a-=1
else:
    b-=1
if s[1] == "<":
    a-=1
else:
    c-=1
if s[2] == "<":
    b-=1
else:
    c-=1

# 別解 あり得る全通り
brothers=[[a,"A"],[b,"B"],[c,"C"]]
brothers.sort()
print(brothers[1][1])

s=input().split()
if s[0] == "<":
    if s[1] == "<":
        if s[2] == "<":
            brothers=["A","B","C"]
        else:
            brothers=["A","C","B"]
    else:
        brothers=["C","A","B"]
else:
    if s[1] == "<":
        brothers=["B","A","C"]
    else:
        if s[2] == "<":
            brothers=["B","C","A"]
        else:
            brothers=["C","B","A"]
print(brothers[1])
"""
# lv2
"""
n,m=map(int,input().split())
son=[False]*n
for i in range(m):
    a,b=input().split()
    if b == "M" and not son[int(a)-1]:
        son[int(a)-1] = True
        print("Yes")
    else:
        print("No")
"""
# lv3
"""
"""
n=int(input())

all=set()
g=[]
gm=int(input())
for _ in range(gm):
    u,v=map(int,input().split())
    g.append((u,v))
    all.add((u,v))

h=[]
hm=int(input())
for _ in range(hm):
    u,v=map(int,input().split())
    h.append((u,v))
    all.add((u,v))

how_much=[]
for i in range(n-1):
    a=list(map(int,input().split()))
    how_much.append(a)

print(how_much)
print(g)
print(h)
pay=0
for i in range(gm):
    print(g[i],g[i] in h)
    u,v=g[i]
    if g[i] in h:
        print("correct:in")
    else:
        print("wrong:not in")
        print("pay",how_much[u-1][v-u-1])
        pay+=how_much[u-1][v-u-1]

for i in range(hm):
    print(h[i],h[i] in g)
    u,v=h[i]
    if h[i] in g:
        print("correct:in")
    else:
        print("wrong:not in")
        print("pay",how_much[u-1][v-u-1])
        pay+=how_much[u-1][v-u-1]
print(pay)