num = 123456

arr = []

while num > 0:
    arr.append(num % 10)
    num //= 10

print(arr)
