n = 200001

A = [True for i in range(n)]

for i in range(2, int(n**0.5)):
    if A[i] == True:
        for j in range(i**2, n, i):
            A[j] = False

B = [i for i in range(2, n) if A[i] == True]

print(B)
print(len(B))
print(B[10000])
