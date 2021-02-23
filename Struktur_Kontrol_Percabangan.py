# Nama : Handro Haturi
# NIM : 71200590
# Grub B
# Universitas Kristen Duta Wacana

# Struktur Kontrol Percabangan

""" Mathea sedang pusing dengan tugas matematika dia. Tugas tersebut ialah mencari 
sebuah luas sigitiga, luas lingkaran, volume tabung. Bantulah Mathea dengan 
sebuah program sederhana jika :
    a. Sebuah segitiga tumpul dengan panjang alas 8 cm dengan tinggi 3 cm, maka 
        berapa luas dari segitiga tersebut?
    b. Sebuah pesawat menjatuhkan bom. Bom tersebut meledak secara sempurna 
        membentuk lingkaran dengan radius ledakan 7 km. Berapakah luas daerah yang 
        terkena dampak ledakan?
    c. Terdapat sebuah tabung yang akan diisi air dengan jari – jari sepanjang 7 cm 
        dan tinggi 30 cm. Tentukanlah volume air yang bisa mengisi penuh tabung tersebut.

Tetapi program ini hanya dapat di akses oleh Mathea.

Rumus :
    a. Segitiga (L = 1/2 * a * t)
        L = Luas Segitiga
        a = Panjang alas segitiga
        t = Tinggi segitiga
    b. Lingkaran (L = π * r^2)
        L = Luas Lingkaran 
        π = Konstanta (3,14 atau 22/7)
        r = jari-jari atau radius
    c. Tabung (V = π * r^2 * t)
        V = Volume tabung
        π = Konstanta (3,14 atau 22/7)
        r = jari-jari atau radius
        t = tinggi tabung

Input :a. Segitiga ( panjang alas = 8cm, tinggi = 3cm)
        b. Lingkaran ( Radius atau jari jari = 7 km)
        c. tabung ( jari jari = 7cm , tinggi = 30 cm)

Proses :a. Segitiga (L = 1/2 * a * t)
        b. Lingkaran (L = π * r^2)
        c. tabung (V = π * r^2 * t)

Output : a. luas segitiga adalah ... cm^2
        b. Luas ledakan tersebut adalah ... km^2
        c. Volume air yagn bisa mengisi tabung hingga penuh adalah ... cm^3

"""
list=["mathea"]
a = str("segitiga")
b = str("lingkaran")
c = str("tabung")

user = input("Masukan nama user anda : ")
print("\n")
if user in list :
    print(f"Selamat datang {user} di program matematika")
    print("\n")
    pilihan = input("Masukan jenis bidang : ")
    if pilihan == a :
        print("Rumus segitiga (L = 1/2 * a * t)")
        print("L = Luas Segitiga")
        print("a = Panjang alas segitiga")
        print("t = Tinggi segitiga")
        a_s = int(input("Masukan panjang alas segitiga = "))
        t_s = int(input("Masukan tinggi segitiga = "))
        rumus_segitiga = ((1/2)*a_s*t_s)
        print (f"Luas segitiga tersebut adalah {rumus_segitiga} cm^2")
    elif pilihan == b :
        print("Rumus lingkaran (L = π * r^2)")
        print("L = Luas Lingkaran")
        print("π = Konstanta (3,14 atau 22/7)")
        print("r = jari-jari atau radius")
        r_l = int(input("Masukan radius ledakan = "))
        rumus_lingkaran = ((22/7)*r_l*r_l)
        print(f"Luas ledakan tersebut adalah {rumus_lingkaran} km^2 ")
    elif pilihan == c :
        r_t = int(input("Masukan jari jari tabung = "))
        t_t = int(input("Masukan tinggi tabung = "))
        rumus_tabung = ((22/7)*r_t*r_t*t_t)
        print (f"Volume air jika tabung adalah {rumus_tabung} cm^3")
else :
    print("ANDA BUKAN USER ")