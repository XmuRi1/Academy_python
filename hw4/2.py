
def nod(a, b):
    if a!=0 and b!=0:
        if a > b:
            a = a % b
            return nod(a, b)
        else:
            b = b % a
            return nod(a, b)
    else:
        return a + b


a = int(input())
b = int(input())

print(nod(a, b))