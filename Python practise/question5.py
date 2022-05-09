#Print the letter k

a=3

for i in range(0,7):
    if i<4:
        for j in range(0,4):
            if j==0:
                print("* ",end="")
            elif j==a:
                print("* ",end="")
                a=a-1;
            else:
                print("  ",end="")
        print("\n")
    else:
        for j in range(0,4):
            if j==0:
                print("* ",end="")
            elif j==a+1:
                print("* ",end="")
            else:
                print("  ",end="")
        print("\n")
        a=a+1