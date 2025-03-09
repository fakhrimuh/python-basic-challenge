jumlah = int(input("Berapa tugas yang ingin anda masukan: "))

tugasList = []
for i in range (jumlah):
    while True:
        tugas = input("Masukan tugas : ").strip()
        if tugas: 
            tugasList.append(tugas)
            print("Tugas Berhasil dimasukkan")
            break

        else:
            print("Tugas gagal dimasukan karena tidak mengandung elemen apapun")
            continue
            
    
print("Daftar Tugas Anda")
for i, tugas in enumerate(tugasList, start=1):    
    print(f"{i}. {tugas}")
