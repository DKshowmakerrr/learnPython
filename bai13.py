n = int(input("nhap vao 1 so tu 1 den 99: "))
while n < 1 or n > 99:
    n = int(input("nhập lại n, n chỉ được phép từ 1 den 99: "))
print(f"số bạn vừa nhập là {n}")