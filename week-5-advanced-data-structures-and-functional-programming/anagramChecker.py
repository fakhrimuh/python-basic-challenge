word1 = input("masukkan kata: ")
word2 = input("Masukkan kata kedua: ") 

cleanWord1 = word1.lower().replace(" ","")
cleanWord2 = word2.lower().replace(" ","")

if not cleanWord1 or not cleanWord2:
    print("Anda belum memasukan karakter apapun")
else:
    if len(cleanWord1) != len(cleanWord2):
        print("Kata tidak mengandung anagram karena jumlah huruf yang berbeda")
    else:
        if sorted(cleanWord1) == sorted(cleanWord2):
            print("Kata mengandung anagram")
        else:
            print("Kata bukan anagram")