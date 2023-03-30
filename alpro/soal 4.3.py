kalimat = input("masukan kalimat: ").lower()
pisah = kalimat.split(' ')
disatukan = ''
for perkata in pisah:
    if perkata.isalpha():
        disatukan += perkata
        disatukan += " "

print(f'hasilnya "{disatukan}\b"')


