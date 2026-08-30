t = int(input())

for t in range(t):
    n, c = map(int, input().split())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    possible = True
    cost1 = 0

    for i in range(n):
        if a[i] < b[i]:
            possible = False
            break
        cost1 += a[i] - b[i]

    if not possible:
        cost1 = float('inf')

    a.sort()
    b.sort()

    possible = True
    cost2 = c

    for i in range(n):
        if a[i] < b[i]:
            possible = False
            break
        cost2 += a[i] - b[i]

    if not possible:
        cost2 = float('inf')

    answer = min(cost1, cost2)

    if answer == float('inf'):
        print(-1)
    else:
        print(answer)
