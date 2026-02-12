n=int(input("Enter rows:"))
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or (i<=n//2 and i==j) or (i<=n//2 and j==n-i-1):
            print("*",end='')
        else:
            print(" ",end='')
    print()