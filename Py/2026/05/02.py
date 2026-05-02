#LvA
"""
X = int(input())

ans = "No"
for i in range(1,7):
    for j in range(1,7):
        for k in range(1,7):
            if i + j + k == X:                
                ans = "Yes"

print(ans)
"""

#LvB
"""
diceList = []
for i in range(3):
    diceList.append(list(map(int,input().split())))
#print(diceList)

ans = 0
for diceOne in diceList[0]:
    for diceTwo in diceList[1]:
        for diceThr in diceList[2]:
            outputDice = {diceOne , diceTwo , diceThr}
            if 4 in outputDice and 5 in outputDice and 6 in outputDice:
                ans += 1
            else:
                continue

#print(ans)
print(ans/6 ** 3)
"""

#LvC
"""
"""
S = input()
N = len(S)

continuePuls = 0
frontS = ""
ans = 0
for i in range(N):
    if S[i] != frontS:
        continuePuls += 1
    else:
        continuePuls = 1
    frontS = S[i]
    ans += continuePuls
print(ans)


#LvD
"""
"""