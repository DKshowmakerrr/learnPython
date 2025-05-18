import time
ten = input("nhập vào tên: ")
tuoi = int(input("nhập vào tuổi: "))
htai = time.localtime()
nam = htai.tm_year
print(f"năm {ten} đạt 100 tuổi là: ", (100-tuoi)+nam)