t = int(input())
 
for t in range(t):
    n = int(input())
    a = list(map(int, input().split()))
 
    ans = 0
 
    for i in range(n):
        if ans > a[i]:
            ans = ans + a[i]
        else:
            ans = a[i]
 
    print(ans)