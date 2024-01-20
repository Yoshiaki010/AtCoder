"""
#lv1
n=int(input())
t=0
a=0
for _ in range(n):
    x,y=map(int,input().split())
    t+=x
    a+=y
if t > a:
    print("Takahashi")
elif t < a:
    print("Aoki")
else:
    print("Draw")
"""
#lv2
s=input()
a=0
b=0
c=0
ans="No"
for i in range(len(s)):
    if s[i] == "A":
        a+=1
    if s[i] == "B":
        b+=1
    if s[i] == "C":
        c+=1
new="A"*a+"B"*b+"C"*c
if new == s:
    ans="Yes"
print(ans)