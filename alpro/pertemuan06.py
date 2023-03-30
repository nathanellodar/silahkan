def pagar_vertical(n):
    print("Output vertical")
    for i in range(n):
        print("#")
    print() #beri jarak

def pagar_horizontal(n):
    print("output horizontal")
    for i in range(n):
        print("#", end=" ")
    print() #beri jarak

def pagar_persegi(n):
    print("pagar persegi")
    for baris in range(n):
        for kolom in range(n):
            print("#", end="")
        print()
    print()

def persegi_bolong(n):
    print("persegi bolong")
    for baris in range(1, n+1):
        if baris == 1 or baris == n:
            for i in range(n):
                print("#", end="")
        else:
            spasi = n - 2
            print("#", end="")
            for i in range(spasi):
                print(" ", end="")
            print("#", end="")
        print()
    print()

def huruf_x(n):
    print("pagar x")
    for baris in range(1, n+2):
        for kolom in range(1, n+1):
            if baris == kolom:
                print("#", end="")
            elif kolom + baris == n+1 :
                print("#", end="")
            else:
                print(" ", end="")
        print()
    print()

def huruf_z(n):
    print("pagar z")
    for baris in range (1, n+1):
        for kolom in range(1, n+1):
            if baris == 1 or baris == n:
                print("#", end="")
            elif baris + kolom == n + 1:
                print("#", end="")
            else:
                print(" ", end="")
        print()
    print()

def huruf_n(n):
    print("pagar N")
    for baris in range(1, n+1):
        for kolom in range(1, n+1):
            if kolom == 1 or kolom == n:
                print("#", end="")
            elif baris == kolom:
                print("#", end="")
            else:
                print(" ", end="")
        print()
    print()
    
def simbol_plus(n):
    print("# plus")
    tengah = (n // 2) + 1
    for baris in range(1, 1+n):
        for kolom in range(1, 1+n):
            if kolom == tengah or baris == tengah:
                print("#", end="")
            else:
                print(" ", end="")
        print()
    print()
            
def segitiga_kiri(n):
    for baris in range(1, n+1):
        for kolom in range(1, baris+1):
            if baris == 1:
                print("#", end="")
            else:
                print("#", end="")
        print()

def segitiga_kanan(n):
    for baris in range(1, n+1):
        pagar = baris
        spasi = n - pagar
        for kolom in range(spasi):
            print(" ", end="")
        for kolom in range(pagar):
            print("#", end="")
        print()
    print()

def jajar_genjang(n):
    for baris in range(1, n +1):
        spasi = n - baris
        pagar = 2 * n - 1
        for kolom in range(spasi):
            print(" ", end="")
        for kolom in range(pagar):
            print("#", end="")
        print()
def segitiga_tengah(n):
    for baris in range(1, n+1):
        spasi = n - baris
        pagar = (2*baris) - 1
        for i in range(spasi):
            print(" ", end="")
        for i in range(pagar):
            print("#", end="")
        print()
    print()

def zig_zag(n):
    for baris in range(1, n+1):
        for kolom in range(1, n+1):
            if baris % 2 != 0:
                    print("#", end="")
            elif baris % 4 == 0:
                print("#", end="")
                break
            else:
                if kolom == n:
                    print("#", end="")
                else: 
                    print(" ", end="")
        print()
    print()




n = int(input("masukan n: "))
pagar_vertical(n)
pagar_horizontal(n)
pagar_persegi(n)
persegi_bolong(n)
huruf_x(n)
huruf_z(n)
huruf_n(n)
simbol_plus(n)
segitiga_kiri(n)
segitiga_kanan(n)
jajar_genjang(n)
segitiga_tengah(n)
zig_zag(n)