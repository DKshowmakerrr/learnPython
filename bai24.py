def f(n):
    if (n == 1 or n == 2):
        return 1
    else:
        return f(n-1)+f(n-2)

print(f(12))

n = int(input("nhap vao n: "))
for i in range(1,n+1,1):
    print(f(i))
