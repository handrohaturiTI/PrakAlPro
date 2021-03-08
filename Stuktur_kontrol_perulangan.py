# Handro Haturi
# 71200590
# Universitas Kristen Duta Wacana

#Struktur Kontrol Perulangan

"""
Dimas adalah anak yang sulit menginat nama teman nya yang baru saja dia kenali. Oleh karena
itu bantulah dimas dalam membuat program yang dapat menyimpan nama nama teman baru nya. Dan
program tersebut akan menampilkan data teman teman nya ketika dia menginput stop.


input: 1. masukan nama

Proses: 1. melakukan perulangan sebanyaka mungkin, sebelum penginput menginput stop, dan jika
            inputan nya stop maka dia akan menampilkan nama nama yang sudah di input.

Output: list nama nama yang sudah di input.

"""

listnama=[]
banyak=0
print("=====SELAMAT DATANG DI PROGRAM PENCATAT NAMA=====")
while True :
    nama = input("Masukan nama: ")
    if nama != "stop":
        listnama.append(nama)
        banyak = len(listnama)
    else :
        break
print("=========LIST NAMA TEMAN ANDA ADA DI BAWAH========")
for i in range(banyak):
    print(f"{i+1}. {listnama[i]}")
print("\n")
