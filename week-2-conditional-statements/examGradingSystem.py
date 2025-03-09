nilai = int(input("Masukkan nilai: "))

if 0 <= nilai <= 39:
    print(f"nilai sebesar {nilai} masuk pada Grade E")
elif 40 <= nilai <= 59 :
    print(f"nilai sebesar {nilai} masuk pada Grade D")
elif 60 <= nilai <= 74 :
    print(f"nilai sebesar {nilai} masuk pada Grade C")
elif 75 <= nilai <= 89 :
    print(f"nilai sebesar {nilai} masuk pada Grade B")
elif 90 <= nilai <= 100 :
    print(f"nilai sebesar {nilai} masuk pada Grade A")
else :
    print(f'nilai {nilai} tidak masuk kriteria manapun')