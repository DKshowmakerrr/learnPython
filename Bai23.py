def giaiThua(n):
    if n == 0:
        return 1
    else:
        return n * giaiThua(n-1)

a = giaiThua(8)
print(a)


