#lv1
"""
N = int(input())
ans = 2 ** N - 2 * N
print(ans)
"""
#lv2
"""
"""
#int(input())
yes = []
no = []
for i in range(1,2026):
    N = i
    print(N, end = " = ")

    next = list(str(N))
    next_int = N
    for _ in range(10):
        if next_int == 1:
            yes.append(N)
            break
        else:
            next_int = 0
            for i in range(len(next)):
                next_int += int(next[i]) ** 2
            next = list(str(next_int))
    else:
        no.append(N)
    print(next_int)

print(yes[:100],len(yes))
print(no[:100],len(no))
#lv3
"""
"""

#lv4
"""
"""
