# Handro Haturi
# Grub B
# 71200590
# Universitas Kristen Duta Wacana

#files

"""
Adi seorang pegawai kantor pos. Karena pengiriman banyak adi 
sering lupa akan alamat yang akan di tuju. sebagai seorang 
teman Adi, saya akan membantu dia membuat program yang akan 
di simpan hasil inputan dia kedalam notepad.

input: nama penerima, alamat penerima, jumlah paket yang akan
kirim

proses: hasil inputan akan di masukan dan di simpan ke dalam
notepad

output: menampilkan nama penerima, alamat penerima yang berada 
di dalam notepad

"""

notepad = open("laporan.txt","w")
print("=====DATA PENGIRIMAN PAKET=====")
a = int(input("Berapa total pengiriman hari ini: "))
for i in range(a):
    a1 = input("Masukan nama penerima: ")
    a2 = input("Masukan alamat penerima: ")
    if len(a1) <= 8 :
        a3= ("Nama Penerima\t\t\tAlamat Penerima\n")
        notepad.write(a3)
        a4 = (f"{a1}\t\t\t\t{a2}\n")
        notepad.write(a4)
    elif len(a1) > 8:
        a3= ("Nama Penerima\t\t\tAlamat Penerima\n")
        notepad.write(a3)
        a4 = (f"{a1}\t\t\t{a2}\n")
        notepad.write(a4)
notepad.close()