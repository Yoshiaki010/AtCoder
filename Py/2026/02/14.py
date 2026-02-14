#lvA
"""
S = input()

ans = "Unknow"
if S[0] == S[-1]:
    ans = "Yes"
else:
    ans = "No"
print(ans)
"""

#lvB
"""
N = int(input())
S = []

m = 0
for _ in range(N):
    Si = input()
    if m < len(Si):
        m = len(Si)
    else:
        pass
    S.append(Si)

for i in range(N):
    t = S[i]
    if len(S[i]) < m:
        k = (m - len(S[i])) // 2
        t = "." * k + S[i] + "." * k
    else:
        pass
    print(t)
"""

#lvC
"""
"""
N = int(input())
A = list(map(int,input().split()))

for i in range(N):
    s = i
    next = 0
    loop_s = 0
    walked = set()
    for _ in range(N):
        if s not in walked:
            next = A[s] - 1
            walked.add(s)
            s = next
        else:
            loop_s = s
            break

#    print(loop_s, walked)

    loop_n = 0
    s = loop_s
    next = 0
    for _ in range(N):
        next = A[s] - 1
        loop_n += 1
        if loop_s == next:
            break
        else:
            continue

#    print(loop_n)

    k = 10 ** 100
#    print(k)

    s = i
    next = 0
    for _ in range(N):
#        print(f"walk to {s}")
        next = A[s] - 1
        s = next
        k -= 1
        if next == loop_s:
            break
        else:
            continue

#    print(s,k)

    k = k % loop_n

#    print(k)

    s = loop_s
    next = 0
    for _ in range(k):
        next = A[s] - 1
        s = next

    ans = s
    print(ans + 1, end = " ")