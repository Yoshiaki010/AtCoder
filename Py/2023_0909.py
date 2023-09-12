"""
#lv1
n=input()
rank=["tourist","ksun48","Benq","Um_nik","apiad","Stonefeang","ecnerwala","mnbvmar","newbiedmy","semiexp"]
ranknum=[3858,3679,3658,3648,3638,3630,3613,3555,3516,3481]
ans="No"

for i in range(len(rank)):
    if n == rank[i]:
        ans=ranknum[i]
        break
print(ans)
"""
"""
#lv2
n=int(input())
ans=[]
for i in range(n+1):
    for j in range(9):
        j+=1
        if i%(n/j) == 0:
            ans.append(j)
            break
    else:
        ans.append("-")
for i in ans:
    print(i ,end="")
"""
#lv3
import math
c=[]
for i in range(3):
    c+=list(map(int,input().split()))
dobulenum=1
all=math.perm(9,9)

def jyunretu(x):
    if len(c)
sad=0

for i in len(c):
ans=(all-sad)/all

print(c)
print(all-sad)
print(sad)
print(ans)




