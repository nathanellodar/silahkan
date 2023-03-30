
# # input
# masukan = input("Masukan Angka (0-9999): ")
# # proses
# # cara pertama
# ribuan = masukan // 1000
# ratusan = (masukan%1000) // 100
# puluhan = (masukan%100)//10
# satuan = masukan%10
# total = ribuan+ratusan+puluhan+satuan
# cara ke 2
# total = 0
# for digit in masukan:
#     total = total + int(digit)
# # output
# print('total semua digit: ', total)

# kurs mata uang
# input
# rupiah = int(input("Masukan Nominal yang akan di Konvert: Rp."))
# # proses
# usd = 14_900
# yen = 130
# eur = 16_700
# aud = 11_500

# ke_usd = rupiah/usd
# ke_yen = rupiah/yen
# ke_eur = rupiah/eur
# ke_aud = rupiah/aud
# # output
# print('Rupiah\t\tUSD\tYEN\tEUR\tAUD')
# print('%d,\t\t%.2f\t%.2f\t%.2f\t%.2f'%(rupiah, ke_usd, ke_yen, ke_eur, ke_aud))
