def MarkChecker(row):
    noMark = 0
    for i in row:
        if i == ".":
            noMark += 1
    return noMark

ans = 6
paper = []
for _ in range(5):
    paper+=list(input())    

#縦
for i in range(5):
    row = paper[i * 5:i * 5 + 5]
    ans = min(MarkChecker(row),ans)

#横
for j in range(5):
    col = paper[j::5]
    ans = min(MarkChecker(col),ans)

#斜め
leftTop = []
rightTop = []
for i in range(5):
    pos = i * 6
    leftTop.append(paper[i * 6])
    rightTop.append(paper[(i + 1) * 4])

ans = min(MarkChecker(leftTop), ans)
ans = min(MarkChecker(rightTop), ans)

print(ans)