nilai = 345
res = 0

while nilai == 0:
    a = nilai % 10
    res = res + a
    nilai = int(nilai/10)
print(res)