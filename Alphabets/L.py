n=int(input("Enter rows:"))
for i in range(n):
    for j in range(n):
        if j==0 or i==n-1:
            print("*",end='')
        else:
            print(" ",end='')
    print()