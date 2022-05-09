#print the letter N

for i in range(0,4):
    for j in range(0,5):
        if j==0 or j==3 or i==j:
            print("*  ",end="")
        else:
            print("   ",end="")
    print("\n")