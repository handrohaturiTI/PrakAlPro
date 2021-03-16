# Handro Haturi
# 71200590
# Universitas Kristen Duta Wacana

# Struktur Kontrol Kompleks
""" 
Mathea ingin membuat sebuah catatan untuk barang yang akan di balanjakan 
dia, tetapi tidak mungkin dia akan membawa catatan kemana mana saat
berbelanja. Oleh karena itu buat lah program yang dapat menyimpan data
belanjaan mathea dan mengurangi data belajaan dia. Dan ketika mathea 
menginput exit dia akan di beritahu barang belanjaan yang dia ambil.


Input : barang yang akan di masukan ke keranjang, barang yang akan di keluarkan dari 
        keranjang, exit untuk menampilkan dan memberhentikan program.

Proses : melaukan perualangan samapai si penginput menginput exit dan kemudian akan 
            menampilkan keranajang. serta menambah atau mengurangi data dari keranjang.

Output : hasil barang yang sudah di masukan ke keranjang.

"""

keranjang = []

while True:
    print("1. Tambah barang ke keranjang")
    print("2. Kurangi barang dari keranjang")
    print("3. Exit")
    user = int(input("Masukan pilihan anda: "))
    if user == 1 :
        masuk = input("Masukan barang ke keranjang: ")
        akhir = keranjang.append(masuk)
        print(f"{keranjang},")
    elif user == 2:
        keluar = input("keluarkan barang dari keranjang: ")
        akhir = keranjang.remove(masuk)
        print(f"{keranjang},")
    elif user == 3:
        print("Barang yang sudah anda masukan ke dalam keranjang")
        for i in range (len(keranjang)):
            print(f"{i+1}. {keranjang[i]}")
        break
    else :
        print("Inputan anda, salah coba kembali")