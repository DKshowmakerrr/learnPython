while True:
    hten = input("nhap ten: ")
    mhoc = input("nhap mon hoc: ")
    diem = float(input("nhap diem: "))
    print(f"hoc sinh {hten}, dự thi môn {mhoc}, có số điểm {diem}")
    if diem >= 7:
        print("xếp loại điểm: Đạt")
    else:
        print("xếp loại điểm: Ko đạt")
    hoi = input("nhập n để thoát, hoặc bất phím bất kỳ để tiếp tục: ")
    if hoi == "n" or hoi == "N":
        break

    #bai 13: xong