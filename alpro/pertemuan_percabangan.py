# suhu = float(input("Masukan Suhu: "))

#  # boolean expression
# if suhu < 32 :
#     print("meninggal")
# elif 32 <= suhu < 36:
#     print("Bahaya Hiportemia")
# elif 36 <= suhu < 38:
#     print("normal")
# elif 38 <= suhu < 41:
#     print("demam")
# else:
#     print("meinggal")#---> jika false

# bilangan negatif positif

# bilangan = int(input('Masukan angka: '))

# if bilangan > 0:
#     print("bilangan positif")
# elif bilangan < 0:
#     print("bilangan negatif")
# else:
#     print("bilangan nol")

# near ten

# bilangan = int(input("Masukan bilangan: "))

# satuan = bilangan % 10

# if satuan in [0,1,2,8,9]:
#     print(True)
# else:
#     print(True)

# ubin

ubin1 = int(input("Masukan Ubin 1 m: "))
ubin5 = int(input("Masukan Ubin 5 m: "))
panjang = int(input("Masukan Panjang yang ingin ditutup: "))

total_ubin5 = ubin5 * 5
total_panjang = ubin1*1 + total_ubin5
if total_panjang >= panjang:
    if panjang // 5 <= ubin5 and (panjang % 5 == 0):
        print("bisa")
    elif (panjang % 5) <= ubin1:
        print("bisa")
    else:
        print("tidak bisa")
else:
    print("tidak")

# nama paling panjang

# nama1 = input("Masukan Nama 1: ")
# nama2 = input("Masukan Nama 2: ")
# nama3 = input("Masukan Nama 3: ")

# if len(nama1) > len((nama2 and nama3)):
#     print("Yang terbesar: ", nama1)
# elif len(nama2) > len((nama1 and nama3)):
#     print("Yang terbesar: ", nama2)
# else:
#     print("Yang terbesar: ", nama3)

# a = int(input("Masukan Angka 1: "))
# b = int(input("Masukan Angka 2: "))
# c = int(input("Masukan Angka 3: "))

# if a != b and a != c:
#     print(a+b+c)
# elif a == b:
#     print(c) 
# elif c == b:
#     print(a)
# elif a == c:
#     print(b)
# else:
#     print(1)
