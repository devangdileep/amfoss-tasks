t = int(input())

for t in range(t):
    n = int(input())
    ans = []
    for i in range(1, n + 1):
        ans.append((2 * i + 1) * (2 * i + 3))

    print(*ans)
