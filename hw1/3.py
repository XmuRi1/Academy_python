n = int(input())
lenth = len(str(n))
sum = 0
buf = 10

while buf > 9:
    while (n // 1) > 0:
        sum+=n%10
        n = n // 10
    buf = sum
    n = sum
    sum = 0

print(buf)