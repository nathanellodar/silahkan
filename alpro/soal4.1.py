kata1 = input("masukan kata satu: ").lower()
kata2 = input("masukan kata dua: ").lower()
for perkata in kata2:
    if perkata in kata1:
        print("anagram")
        break
    else:
        print("bukan anagram")
        break