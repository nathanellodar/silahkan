# menghitung huruf vokal

def hitung_hvokal(kalimat):
    list_vokal = 'aiueoAIUEO' # daftar huruf vokal
    total = 0
    for karakter in kalimat: # cek satu - persatu
        if karakter in list_vokal: # jika ada yang termasuk vokal masuk ke dalam hitungan
            total += 1
    return total

# hitung whitespace
def hitung_karakter_aneh(kalimat):
    total = 0
    for karakter in kalimat:
        if karakter.isspace() == True:
            total += 1
    return total

# hitung konsonan
def hitung_konsonan(kalimat):
    # konsonan adalah alfabet (a - z, (A - Z)) - vokal (aiueo AIUEO)
    list_vokal = 'aiueoAIUEO'
    total = 0
    for karakter in kalimat:
        if karakter not in list_vokal and karakter.isalpha(): # .isalpha maksudnya membatasi lagi yang dicek adalah karakter yang termasuk dalam alphabet
            total += 1
    return total

# program utama
# input
kalimat = input("masukan bilangan: ")

# proses
jumlah_vokal = hitung_hvokal(kalimat)
jumlah_whitespace = hitung_karakter_aneh(kalimat)
jumlah_konsonan = hitung_konsonan(kalimat)
# output
print(f'jumlah huruf vokal = {jumlah_vokal}')
print(f'jumlah white space= {jumlah_whitespace}')
print(f'jumlah huruf konsonan= {jumlah_konsonan}')


