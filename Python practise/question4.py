#print the letter I

for i in range(0,5):
    for j in range(0,5):
        if i==0 or j==2 or i==4:
            print("*  ",end="")
        else:
            print("   ",end="")
    print("\n")