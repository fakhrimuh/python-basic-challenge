genap = []
ganjil = []

while True:
    angka = input("Masukan angka: ").lower().strip()
    try:
        if  angka == 'selesai':
            break
        else:
            angka = int(angka)
            if angka % 2 == 0:
                genap.append(angka)
                print(f'{angka} adalah bilangan genap')
            
            elif angka % 2 != 0:
                ganjil.append(angka)
                print(f'{angka} adalah bilangan ganjil')
    except ValueError :
        print("Input tidak valid! Masukkan angka atau ketik 'selesai' untuk keluar.")
        break

print("Daftar bilangan Anda")
print('Bilangan genap : '+' '.join(str(x) for x in genap))
print('Bilangan ganjil : '+' '.join(str(x) for x in ganjil))