def fin():
    print("No")
    exit()
    
N = int(input())
A = input().split()
B = input().split()

# 要素ペア数の一致判定
A_numberNumdict = dict()
B_numberNumdict = dict()
def dictAdd(value, dict):
    if value in dict:
        dict[value] += 1
    else:
        dict[value] = 1
for i in range(N):
    dictAdd(A[i], A_numberNumdict)
    dictAdd(B[i], B_numberNumdict)
for Ai in A_numberNumdict:
    if Ai not in B_numberNumdict or A_numberNumdict[Ai] != B_numberNumdict[Ai]:
        fin()

# 要素の一致とズレる方向判定
isMuch = []
for i in range(N):
    if A[i] == B[i]:
        #[一致（T/F）、ずらせる方向（N=孤立、L=左、R=右、）]
        isMuch.append([True])
        continue
    if -1 < (i - 1):
        padLeft = i - 1
        if A[i] == B[padLeft]:
            isMuch.append([False,"L"])
            continue
    if (i + 1) < N:
        padRight = i + 1
        if A[i] == B[padRight]:
            isMuch.append([False,"R"])
            continue
    isMuch.append([False,"N"])

j = ""
moveDirection = ""
moveBlock = []
for i in range(N):
    if isMuch[i][0]:
        continue

    if isMuch[i][1] == "N":
        if j == "":
            j = A[i]
        else:
            fin()

    if isMuch[i][1] == "L":
        if moveDirection == "" or moveDirection == "L":
            moveBlock.append(A[i])
            moveDirection = isMuch[i][1]
            continue
        if moveDirection == "R":
            # ずらす方向が競合した場合
            fin()

    if isMuch[i][1] == "R":
        if moveDirection == "" or moveDirection == "R":
            moveBlock.append(A[i])
            moveDirection = isMuch[i][1]
            continue
        if moveDirection == "L":
            # ずらす方向が競合した場合
            fin()

print("Yes")

# 答え表示
print(isMuch)
print(j,moveBlock,moveDirection)
for i in range(N):
    if isMuch[i][0]:
        print(A[i], end = " ")
        continue

    if isMuch[i][1] == "N":
        continue

    if isMuch[i][1] == "L":
        print(" ".join(moveBlock) + " " + j)
        exit()

    if isMuch[i][1] == "R":
        print(j + " " + " ".join(moveBlock))
        exit()
