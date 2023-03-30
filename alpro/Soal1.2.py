# soal 1.2

# keuntungan pertama
while True:
    print(8*"~", "Berapa Keuntungan dalam Rp. dan %", 8*"~")
    print()

    banyak1 = int(input("Masukan Berat Emas: "))
    harga1 = int(input("Masukan Harga beli Emas: "))
    hargasekarang1 = int(input("Masukan Harga Emas Sekarang: "))
    modal1 = banyak1*harga1
    keuntungan1 = (banyak1*hargasekarang1)-(modal1)
    persen1 = (keuntungan1/modal1)*100
    print("keuntungan dalam Rp:", keuntungan1)
    print("Dalam Persen:", persen1,"%")

    # keuntungan kedua
    p = str(input("Apakah Anda Membeli Lagi emas?(y/n):"))
    p = p.upper()
    if p== 'Y':
        banyak2 = int(input("Masukan Berat Emas:"))
        harga2 = int(input("Masukan Harga Beli Emas:"))
        hargasekarang2 = int(input("Masukan Harga Emas Sekarang:"))
        modal2 = (banyak2*harga2)+(modal1)
        banyakemas= banyak1+banyak2
        keuntungan2 = (banyakemas*hargasekarang2)-modal2
        persen2 = (keuntungan2/modal2)*100
        print("Keuntungan Anda Sekarang Rp.", keuntungan2)
        print("Dalam Persen:", persen2, "%")
    else:
        print("Mantap Bang!!")
        break

