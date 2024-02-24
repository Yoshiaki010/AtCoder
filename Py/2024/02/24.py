#lv1
"""
s=list(input())
count={s[0]:0}
ans=0
max=1
difabc=0
for i in range(len(s)):
    if s[i] in count:
        count[s[i]]+=1
    else:
        count[s[i]]=1
    if max < count[s[i]]:
        difabc=i
    else:
        continue
for i in range(len(s)):
    if s[difabc] != s[i]:
        ans=i+1
print(ans)
"""
#lv2
"""
n=int(input())
p=list(map(int,input().split()))
count={}
for i in range(n):
    count[p[i]]=i
q=int(input())
for i in range(q):
    a,b=map(int,input().split())
    if count[a] < count[b]:
        ans=p[count[a]]
    else:
        ans=p[count[b]]
    print(ans)
"""
    
#lv3
n=int(input())
s=input()
abcs=""
numabc=0
dicabc={}
nums=[]
for i in range(n):
    if s[i] not in abcs:
        dicabc[s[i]]=numabc
        abcs+=s[i]
        numabc+=1
    else:
        pass
    nums.append(dicabc[s[i]])

q=int(input())
for i in range(q):
    c,d=input().split()
    if c in abcs:
        new=abcs.replace(c,d)
    else:
        continue
    abcs=new

for i in range(n):
    print(abcs[nums[i]],end="")
"""
"""
#lv4
"""
"""
