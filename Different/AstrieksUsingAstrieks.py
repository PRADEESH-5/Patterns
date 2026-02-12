n=int(input("Enter rows:"))
for i in range(n):
    for j in range(n):
        if j==i or j==n-i-1 or i==n//2 or j==n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()