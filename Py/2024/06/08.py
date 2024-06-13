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
print((1+1)%2)
for i in range(3**k):
    for j in range(3**k):
        if i == 0 or j == 0:
            n+="#"
        elif 2 < i and i < 6 and 2 < j and j < 6:
            n+="."
        elif (i-1)%3 == 0 and (j-1)%3 == 0:
            n+="."
        else:
            n+="#"
    n+="\n"
print(n)
