n=int(input("Enter rows:"))
for i in range(n):
    for j in range(n):
        if (i==0 and j<n-2 and j!=0) or (i==n-2 and j<n-2 and j!=n-2 and j!=0) or (i<n-2 and j==0 and i!=0 and i!=n-1) or (i<n-2 and j==n-2 and i!=0) or (i>=n//2 and i==j):
            print('*',end='')
        else:
            print(' ',end='')
    print()