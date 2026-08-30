t = int(input())

for t in range(t):
    s = input()
    before = 0
    after = 0
    for x in s:
        if x == '4':
            continue
        if x == '2':
            before += 1
        else:
            after = max(after, before) + 1

    keep = max(before, after)
    print(len(s) - keep)
