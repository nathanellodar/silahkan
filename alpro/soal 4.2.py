kalimat = input("masukan kalimat: ").lower()
kata = input("masukan kata: ").lower()
pisah = kalimat.split(" ")
total = 0
for perkata in pisah:
    hapus_titik = perkata.strip('.')
    if hapus_titik == kata:
        total += 1
print(total)
    
