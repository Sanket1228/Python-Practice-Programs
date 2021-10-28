n = int(input("Enter length of triangle : "))
boo = bool(int(input("Enter direction of triangle (1 for upward, 0 for downward) : ")))

if boo == True:
    for i in range(1,n+1):
        print("*"*i)
else:
    while n > 0:
        print("*"*n)
        n -= 1

