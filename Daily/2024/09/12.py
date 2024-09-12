# lv2 
"""
code=dict()
code["-----"]="0"
code[".----"]="1"
code["..---"]="2"
code["...--"]="3"
code["....-"]="4"
code["....."]="5"
code["-...."]="6"
code["--..."]="7"
code["---.."]="8"
code["----."]="9"

ans=""

n=int(input())
for _ in range(n):
    ans+=code[input()]
print(ans)
"""
# lv2 
"""
q=int(input())
a=[]
n=0
for _ in range(q):
    s=list(input().split())
    if s[0] == "1":
        a.append(s[1])
        n+=1
    else:
        k=int(s[1])
        print(a[n-k])
"""
# lv3
"""
n,q=map(int,input().split())
num_to_index=dict()
a=[]
for i in range(n):
    num_to_index[i+1]=i
    a.append(i+1)

for _ in range(q):
    x=int(input())
    i=num_to_index[x]
    if i < n-1:
        left=a[i]
        right=a[i+1]
        num_to_index[left]=i+1
        num_to_index[right]=i
        a[i]=right
        a[i+1]=left
    else:
        left=a[i-1]
        right=a[i]
        num_to_index[left]=i
        num_to_index[right]=i-1
        a[i-1]=right
        a[i]=left

for i in range(n):
    a[i]=str(a[i])
print(" ".join(a))
"""
# lv3
"""
n=int(input())
a=list(map(int,input().split()))

b=sorted(a)
adic=dict()
all=0
for i in range(n):
    if b[i] not in adic:
        adic[b[i]]=all+b[i]
    else:
        adic[b[i]]+=b[i]
    all+=b[i]

for i in range(n):
    print(all-adic[a[i]],end=" ")
"""
# lv4
"""
"""
