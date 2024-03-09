#lv1
"""
s=input()
n=len(s)
l=[]
for i in range(n):
    if s[i] == "|":
        l.append(i)
ans=s[0:l[0]]+s[l[1]+1:n]
print(ans)
"""
#lv2
"""
lista=[]
n=0
for i in range(100):
    try:
        a=input()
        n+=1
    except EOFError:
        break
    lista.append(a)
for i in range(n):
    print(lista[n-1-i])
"""
#lv3

n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
anslist=[]
anslistn=0
for i in range(n):
    for j in range(m):
        anslist.append(a[i]+b[j])
        anslistn+=1
l=int(input())
c=list(map(int,input().split()))
q=int(input())
x=list(map(int,input().split()))
for i in range(q):
    for j in range(anslistn):
        y=x[i]-anslist[j]
        if y in c:
            ans="Yes"
            break
        else:
            continue
    else:
        ans="No"
    print(ans)
"""
"""
