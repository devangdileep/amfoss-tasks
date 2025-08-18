t = int(input())
for i in range(t):
    x,y = map(int , input().strip().split())
    if y>x:
        print(x)
    else:
        print(y)