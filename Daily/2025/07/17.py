#lv2
"""
K = int(input())
A,B = input().split()

def change_to_bin(lis, k):
    ans = 0
    n = len(lis)
    for i in range(n):
        ans += k ** i * int(lis[n - i - 1])

    return ans

A_bin = change_to_bin(A, K)
B_bin = change_to_bin(B, K)

ans = A_bin * B_bin
print(ans)
"""
#lv2
"""
"""
N,M = map(int,input().split())
Price = []
Cost = []
Fetuer = []

for i in range(N):
    product = list(map(int,input().split()))
    p = product[0]
    c = product[1]
    f = product[2:]
    print(p, c, f)
    Price.append(p)
    Cost.append(c)
    Fetuer.append(f)

for i in range(N):
    Fetuer[i] = set(Fetuer[i])

print(Price)
print(Cost)
print(Fetuer)

ans = "Unknow"
#ans = 0
for i in range(N):
    for j in range(N):
        if i != j:
            print(Price[i], Price[j], Fetuer[j], Fetuer[i], Fetuer[i] - Fetuer[j], Fetuer[i] - Fetuer[j] == set())
            if Price[i] >= Price[j] and Fetuer[i] - Fetuer[j] == set():
                print(i,j)
                ans = "Yes"
                continue
            else:
                m = Cost[j]
                f = list(Fetuer[j])
                for k in range(m):
                    if f[k] in Fetuer[i]:
                        pass
                    else:
                        continue
                else:
                    continue
                
                print(i,j)
                ans = "Yes"
                break
    else:
        continue
    break

print(ans)

#lv3
"""
"""

#lv3
"""
"""

#lv4
"""
"""
