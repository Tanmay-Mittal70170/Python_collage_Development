N=int(input("enter the number"))
L=[]
for element in range(N):
    number=int(input("enter the number"))
    L.append(number)

search_number=int(input("enter the number"))

for j in L:
    if search_number== j: 
        print(L.index(j))
        break
else:
    print(-1)