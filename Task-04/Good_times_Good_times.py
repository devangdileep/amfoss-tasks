t = int(input())

for t in range(t):
    x = int(input())

    digits = len(str(x))

    y = 10 ** digits + 1

    print(y)
