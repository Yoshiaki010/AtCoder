#A
"""
D,F = map(int,input().split())
ans = (D - F) % 7 
print(7 - ans)
"""
#B
"""
N,M = map(int,input().split())
S = input()
T = input()

ans = (10 ** 4) + 1
for i in range(N - M + 1):
    c = 0
#    print(S[i:i + M], end = " ")
    for j in range(M):
        if T[j] == S[i + j]:
            continue
        else:
            si,ti = map(int,[S[i + j], T[j]])
            if si < ti:
                c +=  si + 10 - ti
#                print(f"{si + 10} - {ti} = +{si + 10 - ti}", end = " , ")
            else:
                c += si - ti
#                print(f"{si} - {ti} = +{si - ti}", end = " , ")
#    print(end = " = ")
    if c < ans:
        ans = c
#    print(c)
print(ans)
"""

#C
"""
"""
N = int(input())
A = list(map(int,input().split()))
oneset = [[A[0],1]]
point = 0
for i in range(1,N):
    k,num = oneset[point]
    if A[i] == k:
        oneset[point][1] += 1
    else:
        oneset.append([A[i],1])
        point += 1
    
ans = 0
serch_tag = [oneset[0]]
for i in range(len(oneset)):
    k,n = oneset[i]
    if n == 4:
        continue


print(oneset)
print(point)
#print(ans)