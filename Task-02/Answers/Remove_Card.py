t = int(input())
for i in range(t):
    n = int(input())
    r = list(map(int , input().split()))
    max_occ = 0
    for i in r:
        if r.count(i) > max_occ:
            max_occ = r.count(i)
    print(n - max_occ)