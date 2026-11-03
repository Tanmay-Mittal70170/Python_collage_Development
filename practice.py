n = int(input("Enter the number of rows: "))

L = []
for i in range(n):
    row = list(map(int, input("Enter row ").split()))
    L.append(row)


rows_sum = [sum(row) for row in L]

column_sum = [sum(row[i] for row in L) for i in range(len(L[0]))]

Max=0

for num in rows_sum:
    if num>Max:
        Max=num
    

total_sum=sum(rows_sum)


print(rows_sum)
print(column_sum)
print(rows_sum.index(Max))
print(total_sum)