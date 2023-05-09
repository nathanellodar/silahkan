nama_toko = "Olivander"
print(f"selamat datang di toko {nama_toko}")
inputan_nama = input("Masukan nama anda: ")
nama_pembeli = inputan_nama
nota = [
    {'nama_barang' : 'wands', 'harga' : 20000, 'jumlah' : 10},
    {'nama_barang' : 'sapu', 'harga' : 65000, 'jumlah' : 7},
    {'nama_barang' : 'jubah', 'harga' : 100_000, 'jumlah' : 2},
    {'nama_barang' : 'topi sihir', 'harga' : 250_000, 'jumlah' : 1}
]

for panggil in nota:
    print(f"{panggil['nama_barang']} - harga satuan {panggil['harga']} - dengan jumlah = {panggil['jumlah']} - Total = {panggil['harga'] * panggil['jumlah']}")
pilihan = input("mau menambah barang?(y/n)").lower()
if pilihan == 'y':
    while True:
        inputan_barang = input("Masukan nama barang yang mau ditambah: ")
        inputan_harga = int(input("Masukan harga: "))
        jumlah = int(input("masukan banyak: "))
        ditambah = {'nama_barang' : inputan_barang, 'harga' : inputan_harga, 'jumlah' : jumlah}
        nota.append(ditambah)
        pilihan = input("mau menambah?(y/n)").lower()
        if pilihan == 'y':
            continue
        else:
            for panggil in nota:
                print(f"{panggil['nama_barang']} - harga satuan {panggil['harga']} - dengan jumlah = {panggil['jumlah']} - Total = {panggil['harga'] * panggil['jumlah']}")
                jumlah_beli = 0
                total_harga = 0
                print(f'Nama toko: {nama_toko}\nNama Pembeli: {nama_pembeli}')
            print(20*"=")
            for beli in nota:
                jumlah_beli += beli['jumlah']
                total_harga += beli['harga']
            print(f'Jumlah barang yang dibeli = {jumlah_beli}\nTotal harga = {total_harga}')
            print(f"harga setelah diskon 20% {total_harga*20/100}")
            break
else:
    for panggil in nota:
        print(f"{panggil['nama_barang']} - harga satuan {panggil['harga']} - dengan jumlah = {panggil['jumlah']} - Total = {panggil['harga'] * panggil['jumlah']}")
        jumlah_beli = 0
        total_harga = 0
    print(f'Nama toko: {nama_toko}\nNama Pembeli: {nama_pembeli}')
    print(20*"=")
    for beli in nota:
        jumlah_beli += beli['jumlah']
        total_harga += beli['harga']
    print(f'Jumlah barang yang dibeli = {jumlah_beli}\nTotal harga = {total_harga}')
    print(f"harga setelah diskon 20% {total_harga*20/100}")

