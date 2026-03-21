#lvA
"""
N = int(input())
ans = [str(N - i) for i in range(N)]
print(",".join(ans))
"""
#lvB
"""
N = int(input())
cost_dic = dict()
for i in range(N - 1):
    cost_dic[i] = list(map(int,[0] + input().split()))
#print(cost_dic)

ans = "Uknow"
for a in range(N):
    for b in range(N):
        if a < b:
            for c in range(N):
                if b < c:
#                    print(a,b,c)
                    ac_cost = cost_dic[a][c - a]
                    abc_cost = cost_dic[a][b - a] + cost_dic[b][c - b]
#                    print(f"a-c : {ac_cost}")
#                    print(f"a-b-c : {abc_cost}")
                    if abc_cost < ac_cost:
                        ans = "Yes"
                    
else:
    if ans == "Uknow":
        ans = "No"
print(ans)
"""
#lvC
"""
"""
H,W = map(int,input().split())
S = [["o"] * (W + 2)]
for _ in range(H):
    S.append(["o"] + list(input()) + ["o"])
S.append(["o"] * (W + 2))

for i in range(H + 2):
    print(S[i])

print()
start_i = 1
start_j = 1
for x in range(H):
    for y in range(W):
        i = start_i + x
        j = start_j + y
        if S[i][j] == ".":
            if S[i + 1][j] == "o" or S[i - 1][j] == "o" or S[i][j + 1] == "o" or S[i][j - 1] == "o":
                S[i][j] = "o"

for x in range(H):
    for y in range(W):
        i = start_i + x
        j = start_j + y
        if S[i][j] == "o":
            S[i][j] = "#"

for i in range(H + 2):
    print(S[i])

arrive_s = []
arrive_s_n = 0
for x in range(H):
    for y in range(W):
        i = start_i + x
        j = start_j + y
        if S[i][j] == ".":
            arrive_s.append((i,j))
            arrive_s_n += 1

print(*arrive_s,arrive_s_n)

blocks = []
blocks_n = 0
for i in range(arrive_s_n):
    for j in range(blocks_n):
        ar_i,ar_j = arrive_s[i]
        if (ar_i + 1, ar_j) in blocks[j] or (ar_i - 1, ar_j) in blocks[j] or (ar_i, ar_j + 1) in blocks[j] or (ar_i, ar_j - 1) in blocks[j]:
            blocks[j].add(arrive_s[i])
            break
    else:
        blocks.append(set())
        blocks[blocks_n - 1].add(arrive_s[i])
        blocks_n += 1

print(blocks,blocks_n)
#lvD
"""
"""
