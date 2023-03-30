kalimat = input("masukan kalimat: ").lower()
pisah = kalimat.split(" ")
penampung = []
for tambah in pisah:
    penampung.append(tambah)
penampung.sort(key=len)
print(penampung[0])
print(penampung[-1])