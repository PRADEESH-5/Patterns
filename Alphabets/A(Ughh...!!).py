n=int(input("Enter Rows:"))
for i in range(n):
    for j in range(n):
        if j==n-i-1 or (j>n//2 and i==n//2):
            print('*',end='')
        else:
            print(' ',end='')
    for k in range(n):
        if k==i or (k<n//2 and i==n//2):
            print('*',end='')
        else:
            print(' ',end='')
    print()