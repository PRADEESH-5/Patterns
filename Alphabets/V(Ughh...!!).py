n=int(input("Enter rows:"))
for i in range(n):
    for j in range(n):
        if i==j:
            print("*",end='')
        else:
            print(" ",end='')
    for k in range(n):
        if k==n-i-1:
            print("*",end='')
        else:
            print(" ",end='')
    print()