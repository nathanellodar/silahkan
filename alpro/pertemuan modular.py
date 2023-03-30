# def tambah(a, b, c):
#     hasil = a + b + c
#     return hasil #jika ingin mempengaruhi program utama atau ini wajib untuk berfungsi
# a = int(input("Masukan Nilai Pertama: "))
# b = int(input("Masukan Nilai kedua: "))
# c = int(input("Masukan Nilai ketiga: "))

# print(tambah(a, b, c))

#digit kiri

# def digit_kanan(a, b, c):
#     if a % 10 == b % 10 == c % 10:
#         print("sama")
#     else:
#         print("tidak sama")
#     return a, b, c

# a = int(input("Masukan bilangan 1: "))
# b = int(input("Masukan bilangan 2: "))
# c = int(input("Masukan bilangan 3: "))

# print(digit_kanan(a, b, c))

# def hari_setelah(hari, ke_berapa):
#     list_hari = ['senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu', 'minggu']
#     no_hari = list_hari.index(hari)
#     maka = ke_berapa % 7
#     total = (no_hari + maka) % 7
#     print(list_hari[total])
# #input hari
# hari = input("masukan hari: ")
# ke_berapa = int(input("Masukan Mau Ke Hari Berapa: "))
# hari_setelah(hari, ke_berapa)

# mencari runner up
p1 = float(input("Masukan Jumlah Waktu 1: "))
p2 = float(input("Masukan Jumlah Waktu 2: "))
p3 = float(input("Masukan Jumlah Waktu 3: "))
p4 = float(input("Masukan Jumlah Waktu 4: "))
p5 = float(input("Masukan Jumlah Waktu 5: "))

# penampung = [p1, p2, p3, p4, p5]
# penampung.sort()
# print(penampung[-2])


runner_up = lambda penampung = [ p1, p2, p3, p4, p5]:  penampung.sort