# Handro Haturi
# 71200590
# Universitas Kristen Duta Wacana

# Set

"""
Saya ingin membuat program yang berisi inputan beberapa data. 
dan inputan itu akan saya masukan ke dalam set. 
Kemudian data tersebut bisa saya rubah, semisal menambahkan data 
lagi dan mengurangi nya.

Input : Menambahkan data dan mengurangi data 

Proses : Perpindahan inputan ke dalam set, Penambahan data dan 
pengurangan

Output : Data yang sudah di rubah dan sebelum di rubah
"""
kosong = set()
data = input("Masukan Data: ").split(",")
for i in data :
    kosong.add(i)
print(f"Data anda adalah {kosong}")
print(" ")

while True:
    print("Pilihan untuk di ubah: ")
    print("1. Tambah data")
    print("2. Kurang data")
    print("3. Exit")
    pilih = int(input("Masukan pilihan anda: "))
    if pilih == 1:
        tambah = input("Tambah data: ")
        kosong.add(tambah)
        print(f"Data anda sekarang adalah {kosong}")
    elif pilih == 2 :
        kurang = input("Kurang data: ")
        kosong.remove(kurang)
        print(f"Data anda sekarang adalah {kosong}")
    elif pilih == 3:
        print("TERIMA KASIH")
        break
    else :
        print("inputan SALAHHHHH")