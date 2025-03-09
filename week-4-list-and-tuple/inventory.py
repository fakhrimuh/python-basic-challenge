inventaris = ["Laptop", "Printer", "Meja", "Kursi"]

while True:
    print('===========================')
    print('========Inventaris=========')
    print('===========================')

    print("1. Tambah Barang")
    print("2. Hapus Barang")
    print("3. Lihat Barang")
    print("4. Keluar")

    try:
        menu = int(input("silahkan pilih menu: "))
        if menu == 1:
            barang = input("masukan nama inventaris: ").strip()
            if not barang:
                print("input barang tidak boleh kosong")
            elif barang in inventaris:
                print("barang sudah ada")
            else:
                inventaris.append(barang)
                print("barang berhasil ditambahkan")

        elif menu == 2:
            if not inventaris:
                print("Anda Tidak Memiliki Inventaris")
                continue
            
            print("Daftar Inventaris Anda")
            for i, inventarisList in enumerate(inventaris, start=1):    
                print(f"{i}. {inventarisList}")

            barang = input("masukan nama inventaris yang ingin dihapus: ").strip()
            if barang in inventaris:
                while True:
                    konfirmasi = input("anda yakin ingin menghapus barang ini (y/n)").lower().strip()
                    if konfirmasi == "y":
                        inventaris.remove(barang)
                        print("Barang berhasil dihapus")
                        break
                    if konfirmasi == 'n':
                        print("barang tidak jadi dihapus")
                        break
                    else:
                        print("Input tidak valid! Masukkan 'y' untuk menghapus atau 'n' untuk batal.")
            else:
                print("Barang tersebut tidak ada di inventaris")
        elif menu == 3:
            if not inventaris:
                print("Anda Tidak Memiliki Inventaris")
            else:
                print("Daftar Inventaris Anda")
                for i, inventarisList in enumerate(inventaris, start=1):    
                    print(f"{i}. {inventarisList}")
        elif menu == 4:
            print("Terimakasih sudah menggunakan program ini")
            break
        else:
            print("Pilihan tidak valid, silahkan pilih angka 1-4")
    except ValueError:
         print("Input tidak valid! Harap masukkan angka 1-4.")
