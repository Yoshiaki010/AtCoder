#lv2
"""
l,r=map(int,input().split())
s=list(input())
for i in range(len(s)):
  if i < l-1 or r-1 < i :
    print(s[i],end="")
  else:
    print(s[(r-1)-(i-(l-1))],end="")
"""
#lv2
n=int(input())
s=[]
ans=0
for _ in range(100):
    sh=[]
    for _ in range(100):
        sh.append(".")
    s.append(sh)
for _ in range(n):
    a,b,c,d=map(int,input().split())
    for y in range(d-c):
        for x in range(b-a):
            if s[y+c][x+a] == ".":
                s[y+c][x+a]="#"
                ans+=1
print(ans)
ans=10
for i in range(9):
    ans*=10-i
print(ans)