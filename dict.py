# Handro Haturi
# 71200590
# Universitas Kristen Duta Wacana

# Dictionaries

"""
Dio adalah seoarang pegawai di bidang pemberi gaji. Nah dio ingin 
saya untuk membuatkan program yang berfungsi untuk menghitung rata2
dari gaji karyawan serta karyawan yang mendapat gaji lebih dari 
rata rata.

input :jumlah karyawan, nama karyawan, gaji karyawan

proses :rata rata gaji dari semua karyawan, gaji karyawan yang lebih
besar dari rata2.

output :rata2 gaji semua karyawan, nama dan gaji karyawan yang lebih dari
rata2
"""

nama = int(input("Masukan jumlah karyawan: "))
a = dict()
hasil = 0
for i in range(nama):
    nama1 = input("Nama karyawan: ")
    gaji = int(input("Gaji karyawan: "))
    print(" ")
    hasil = hasil + gaji
    a[nama1] = gaji

# rata2
rata = hasil/nama
print("================")
print(f"rata-rata gaji karyawan: {rata}")
print("================")
print("Karyawan yang gajinya melebihi rata rata")
val = a.values()
key = a.keys()
for j in val:
    if j > rata :
        for x in key :
            if a[x] == j :
                print(f"{x} : {j}")
