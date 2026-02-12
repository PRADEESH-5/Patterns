n=7
for i in range(n):
    for j in range(n):
        if j==n-2 or i==n-3:
            print("*",end='')
        else:
            print(' ',end='')
    print()