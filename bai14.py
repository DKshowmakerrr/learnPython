# for i in range(2,11,2):
#     print(i)
a = int(input("Nhập vào số a: "))
if a%2 == 0:
    for i in range(1,6,1):
        a=a+1
        print("Tổng a là: ", a)
else:
    print("Tôi không tinh tổng số lẻ, bye bye")