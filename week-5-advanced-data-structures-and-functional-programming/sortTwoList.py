inputList1 = input("Masukkan angka untuk list pertama (pisahkan dengan spasi): ")
inputList2 = input("Masukkan angka untuk list kedua (pisahkan dengan spasi): ")

list1= list(map(int, inputList1.split()))
list2 = list(map(int, inputList2.split()))

mergeList = list1+list2

n = len(mergeList)

for i in range(n):
    already_sorted = True

    for j in range(n - i - 1):
        if mergeList[j] > mergeList[j + 1]:
            mergeList[j], mergeList[j + 1] = mergeList[j + 1], mergeList[j]
            already_sorted = False

    if already_sorted:
        break

print("Hasil setelah diurutkan:", mergeList)