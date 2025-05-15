# lv1
"""
R,G,B = map(int,input().split())
C = input()

ans = "Unknow"
if C[0] == "R":
    if G < B:
        ans = G
    else:
        ans = B
elif C[0] == "G":
    if R < B:
        ans = R
    else:
        ans = B
else:
    if R < G:
        ans = R
    else:
        ans = G
print(ans)
"""
# lv1
"""
"""

# lv2
"""
N = int(input())

tree_dict = dict()
for i in range(N):
    i += 1
    tree_dict[i] = 0

for _ in range(N - 1):
    a,b = map(int,input().split())
    tree_dict[a] += 1
    tree_dict[b] += 1

ans = "No"
for i in range(N):
    i += 1
    if tree_dict[i] == 1 or tree_dict[i] == N - 1:
        continue
    else:
        break
else:
    ans = "Yes"

print(ans)
"""
# lv2
"""
n = int(input())
wallet = list(map(int,input().split()))

for i in range(n - 1):
    s,t = map(int,input().split())
    if wallet[i] >= s:
        wallet[i + 1] += t * (wallet[i] // s)

print(wallet[-1])
"""
# lv3
"""
"""
N = int(input())

bin = []
bin_n = 0
A = N
while 0 < A:
    bin.append(A % 2)
    bin_n += 1
    A //= 2

R = []
next = []
k = bin_n - 1
for _ in range(bin_n - 1):
    if bin[k - 1] == 0:
        R.append(2 ** k)
    else:
        next.append(2 ** k - 1)
    k -= 1

print(R,next)
# lv3
"""
X = input().split()
print(26 ** 10)
"""