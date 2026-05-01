print("\033[31mThis text is red\033[0m")
for i in range(1,11):
    for j in range(1,11):
        print("{:02d}".format(i*j),end=" ")
    print()