"""
#lv1
array={"ACE","BDF","CEG","DFA","EGB","FAC","GBD"}
s=input()
if s in array:
    ans="Yes"
else:
    ans="No"
print(ans)
"""
"""
#lv2
n,m=list(map(int,input().split()))
s=[]

for _ in range(n):
    s+=[list(input())]

for i in range(n-8):
    for j in range(m-8):
        if [s[i][j:j+4],s[i+1][j:j+4],s[i+2][j:j+4],s[i+3][j:j+4]] == [["#","#","#","."],["#","#","#","."],["#","#","#","."],[".",".",".","."]]:
            if [s[i+5][j+5:j+9],s[i+6][j+5:j+9],s[i+7][j+5:j+9],s[i+8][j+5:j+9]] == [[".",".",".","."],[".","#","#","#"],[".","#","#","#"],[".","#","#","#"]]:
                print(i+1,j+1)
"""
"""
"""
#lv3
n,m=list(map(int,input().split()))
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a.sort()

for i in range(len(a)):
    seller=i+1
    buyer=0
    for j in b:
        if a[i] <= j:
            buyer+=1
    if max(b)+1 < min(a):
        x=max(b)+1
        break
    elif seller >= buyer:
        x=a[i]
        break

print(x)