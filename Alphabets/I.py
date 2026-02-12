n=int(input("Enter rows:"))
for i in range(n):
    for j in range(n):
        if i==0 or j==n//2 or i==n-1:
            print("*",end='')
        else:
            print(' ',end='')
    print()