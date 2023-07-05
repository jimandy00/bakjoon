nList = []

for i in range(9):
    nList.append(input())

print(max(nList))
print(nList.index(max(nList))+1)