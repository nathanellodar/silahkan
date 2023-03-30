def enkripsi(kalimat):
    daftar_huruf = 'aAiIeEoOjJgGbrRsSB'
    huruf_enkrip = '441133007799622558'
    hasil = ''
    for karakter in kalimat:
        if karakter in daftar_huruf: # harus di rubah
            posisi = daftar_huruf.index(karakter)
            hasil += huruf_enkrip[posisi]
        else:
            hasil += karakter # tidak perlu dirubah
    return hasil
            
def cek_palindrom(kalimat):
    isi_kalimat = ''
    kalimat = kalimat.lower() # format huruf
    for karakter in kalimat:
        if karakter.isalpha():
            isi_kalimat += karakter # hapus yang bukan alphabet
    
    kalimat_terbalik = isi_kalimat[::-1] # membalikkan kalimat

    if kalimat_terbalik == isi_kalimat: # mengecek kalimat yang telah dibalik
        return True
    else:
        return False
# input

kalimat = input("masukan kalimat: ")
hasil = enkripsi(kalimat)
jawaban_palindrome = cek_palindrom(kalimat)
print(hasil)

if jawaban_palindrome == True:
    print("palindrome")
else:
    print("bukan palindrome")