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
anslistn=int(input())
anslist=list(map(int,input().split()))
for _ in range(2):
    n=int(input())
    a=list(map(int,input().split()))
    new=[]
    newn=0
    for i in range(n):
        for j in range(anslistn):
            new.append(a[i]+anslist[j])
            newn+=1
    anslist=new
    anslistn=newn
q=int(input())
x=list(map(int,input().split()))
for i in range(q):
    if x[i] in anslist:
        ans="Yes"
    else:
        ans="No"
    print(ans)
"""
"""
