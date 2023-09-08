n,q=list(map(int,input().split()))
print(n,q)
nlis=[]
ans=[]
for i in range(n):
    nlis.append(chr(65+i))
for i in range(q):
    print("?"+nlis[0],nlis[1])
    j=input()
    print(j)
    if j == ">":
        ans.append(ans[0])
        ans.remove(ans[0])
    elif j == "<":
        ans.append(ans[0])
        ans.remove(ans[0])


print(ans)
