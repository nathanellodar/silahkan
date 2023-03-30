def pagar_bolong(n):
    for baris in range(1, n+1):
            if baris == 1 or baris == n:
                for tampil in range(1, n+1):
                    print("#", end="")
            else:
                print("#", end="")
                for spasi in range(n-2):
                    print(" ", end="")
                print("#", end="")
            print()
n = int(input("Masukan besar kotak: "))
pagar_bolong(n)