#lv1
"""
n,m=map(int,input().split())
h=list(map(int,input().split()))
ans=0
for i in range(n):
    if m-h[i] < 0:
        break
    else:
        m-=h[i]
        ans+=1
print(ans)
"""
#lv2
"""
s=input()
n=len(s)
big=0
sml=0
for i in range(n):
    if ord(s[i]) < 91:
        big+=1
    else:
        sml+=1
ans=""
if big < sml:
    ans=s.lower()
else:
    ans=s.upper()
print(ans)
"""
#lv3
"""
"""
k=int(input())
n=""

if k-1 == 0:
    n+="#"
elif 0 < k-1:
    oneper=3**(k-1)//3
    for i in range(3**(k-1)):
        if oneper-1 < i and i < oneper*2:
            n+="#"*oneper+"."*oneper+"#"*oneper
        else:
            n+="#"*oneper*3
else:
    pass

oneper=3**k//3
sp="."*oneper
if k == 0:
    print("#")
else:
    for i in range(3**k//oneper):
        if  i == 1:
            for j in range(3**(k-1)):
                print(n[j*(3**(k-1)):(j+1)*(3**(k-1))]+sp+n[j*(3**(k-1)):(j+1)*(3**(k-1))])
        else:
            for j in range(3**(k-1)):
                print(n[j*(3**(k-1)):(j+1)*(3**(k-1))]*3)
