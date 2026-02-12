n=int(input("Enter rows:"))
for i in range(n):
    print(" "*(n-i-1),end=' ')
    m=1
    for j in range(i+1):
        print(m,end=' ')
        m=m*(i-j)//(j+1)
    print()