a1 = "python"
a2 = 'league of legend'
a3 = '''rút đao chém nước, nước càng chảy'''
a4 = """nâng chén tiêu sầu càng sầu thêm"""

print(a1)
print(a2)
print(a3)
print(a4)

print(len(a2))

for i in a2:
    print(i, end="\t")

a = a3 +" " + a4
print(a)

print("-"*40)

print("Ga" in a1)