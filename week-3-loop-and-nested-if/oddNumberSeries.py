angka = int(input('Masukan angka : '))


for i in range(1, angka+1, 2): 
    if i % 2 != 0 :
        print(i)

print("==================")
i = 1
while i <= angka :
    print (i)
    i += 2