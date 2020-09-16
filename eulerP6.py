n = 100000

sum_of_squares = 0
sum = 0

for i in range(n+1):
    sum_of_squares += i**2
    sum += i

print(sum_of_squares)
print(sum)
print(sum**2)
print("Róźnica :", sum**2 - sum_of_squares)
