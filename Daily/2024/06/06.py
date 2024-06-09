#lv2
"""
s=list(input())
ns=len(s)
t=list(input())
nt=len(t)
ans="Unknow"
for i in range(ns):
    if s[i] == t[0]:
        for j in range(nt):
            if ns-1-i < j:
                break
            else:
                if s[i+j] == t[j]:
                    continue
                else:
                    break
        else:
            ans="Yes"
            break
    else:
        continue
else:
    ans="No"         
print(ans)
"""
#lv2
"""
k=int(input())
a,b=input().split()
na=len(a)
nb=len(b)
def change(x,n,h):
    ans=0
    for i in range(n-1):
        ans+=h**(n-i-1)*int(x[i])
    ans+=int(x[-1])
    return(ans)
newa=change(a,na,k)
newb=change(b,nb,k)
ans=newa*newb
print(ans)
"""
#lv3
"""
#print(2**60)
k=int(input())
ans=""
for i in range(60):
    if k == 0:
        break
    else:
        new=""
        if k % 2 == 0:
            new="0"
        else:
            k-=1
            new="2"
        ans=new+ans
        k//=2
print(ans)
"""
#lv3
"""
n=int(input())
s=list(input())
now=False
ans=""
for i in range(n):
    if now:
        if s[i] == '"':
            now=False
        else:
            pass
        ans+=s[i]
    else:
        if s[i] == '"':
            now=True
            ans+=s[i]
        elif s[i] == ",":
            ans+="."
        else:
            ans+=s[i]
print(ans)
"""
#lv4
"""
"""
n=int(input())
s=input()
q=int(input())
for i in range(q):
    t,x,c=input().split()
    print(t,x,c)