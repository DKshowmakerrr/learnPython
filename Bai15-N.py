n = int(input("Nhập vào chiều cao: "))
for i in range(n):
    for j in range(n):
        if j == 0 or j == 6 or i == j:
            print("*", end = "   ")
        else:
            print(" ", end = "   ")
    print()