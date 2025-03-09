while True :
    print('=== Pendaftaran Akun ===')
    username = input('Masukan Username: ')
    password = input('Masukan Password: ')

    if len(password) <= 0 or len(username) <= 0:
        print("password atau username harus diisi")
        continue

    if len(username) > 0 and len(password) > 5:
        print ("Akun berhasil dibuat!")
        percobaan = 3
        while percobaan > 0:
            print('=== Login Akun ===')

            userLogin = input("Masukan Username: ")
            passLogin = input("Masukan Password: ")

            if userLogin == username and passLogin == password:
                print("Login Berhasil")
                break

            else :
                percobaan -=1
                if percobaan > 0 :
                    print(f'Login gagal. Sisa percobaan: {percobaan}' )
                else :
                    print ('Akun Diblokir')
                    break
        break
    
    else:
        print("Password terlalu pendek! Gunakan minimal 6 karakter.")