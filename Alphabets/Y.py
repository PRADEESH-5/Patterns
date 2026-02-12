n=int(input("Enter rows:"))
for i in range(n):
    for j in range(n):
        if (i<n//2) and (i==j or j==n-i-1) or (i>=n//2 and j==n//2):
            print('*',end='')
        else:
            print(' ',end='')
    print()