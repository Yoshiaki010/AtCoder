"""
#lv1
n=int(input())
w=n%5
ans=0

if w==0:
    ans=n
elif w>=3:
    s=5-w
    ans=n+s
elif w<=2:
    ans=n-w

print(ans)

#lv2
point=[3,1,4,1,5,9]
ans=0
p=[ord(i)-65 for i in input().split()]

p.sort()

for i in point[p[0]:p[1]]:
    ans+=i

print(ans)
"""
#lv3
h,w=map(int,input().split())
s=[]
nosnakh=501

k=0
for _ in range(h):
    rsnak=0
    i=list(input())
    for j in i:
        if j =="#":
            rsnak+=1
    if rsnak!=0:
        if nosnakh>=rsnak:
            nosnakp=rsnak
            nosnakh=k
    s.append(i)
    k+=1

print(h,w)
print(s)
print(nosnakh)

for j in range(w):
    if s[nosnakh][j] == ".":
       if s[h-nosnakh+1][j]=="#" or s[h-nosnakh-1][j]=="#":
            nosnakw=i
