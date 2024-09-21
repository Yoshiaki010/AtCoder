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
for i in range(n):
    pay=0
    for j in range(gm):
        u,v=g[j]
        print((u+i,v+i),(u+i,v+i) in h)
        if (u+i,v+i) in h:
            print("correct:in")
        else:
            print("wrong:not in")
            print("pay",how_much[u-1][v-u-1])
            pay+=how_much[u-1][v-u-1]

    for j in range(hm):
        u,v=h[j]
        print((u+i,v+i),(u+i,v+i) in g)
        if (u+i,v+i) in g:
            print("correct:in")
        else:
            print("wrong:not in")
            print("pay",how_much[u-1][v-u-1])
            pay+=how_much[u-1][v-u-1]
    print(pay)
    print()
"""
n=int(input())
g=[]
gm=int(input())
for _ in range(gm):
    u,v=map(int,input().split())
    g.append((u,v))
print("g:",g)

newg=[]
for i in range(n):
    for j in range(n):
        if i < j:
            i+=1
            j+=1
            if (i,j) in g or (j,i) in g:
                newg.append(True)
            else:
                newg.append(False)
print("newg:",newg)

h=[]
hm=int(input())
for _ in range(hm):
    u,v=map(int,input().split())
    h.append((u,v))
print(f"h:{h}")

how_much=[]
for _ in range(n-1):
    a=list(map(int,input().split()))
    how_much.append(a)
print(f"how:{how_much}")

for i in range(n):
    print(f"start:{i}")
    newh=[]
    pay=0
    f=0
    for j in range(n):
        newh=False
        for k in range(n):
            if j < k:
                u=(i+j)%(n)+1
                v=(i+k)%(n)+1
                print(f"u,v:({u},{v})",end=" ")
                if (u,v) in h or (v,u) in h:
                    newh=True
                else:
                    newh=False
            else:
                continue
            print(f)
            if newh == newg[f]:
                continue
            else:
                pay+=how_much[j][k-j]
            f+=1
        print()
    print(pay)
    print(newh)
    print("fin")
    print()
print(f)