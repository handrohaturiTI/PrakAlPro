# Nama : Handro Haturi
# NIM : 71200590
# Grub B
# Universitas Kristen Duta Wacana

#Variable,Expressions, dan Statements

''' Beryl mendapat tugas dari sekolah untuk mata pelajaran fisika. Si beryl bingung untuk 
    menjawab tugas dari sekolah. Soal tersebut adalah Jika sebuah gelombang bergetar sebanyak 
    120 kali selama 1 menit serta panjang gelombangnya 200 centimeter maka berapakah frekuensi 
    dan cepat rambat gelombang tersebut?
    (Rumus : V = lamda * f)
    (f = n / t)

    lamda = panjang gelombang(meter)
    V = cepat rambat gelombang (m/s)
    f   = frekuenasi gelombang (Hz)
    n  = jumlah gelombang
    t   = waktu (sekon)
'''
'''
    Input : lamda = 200cm , n = 120 kali , t = 1 menit

    Proses :
        f = n / t
        V = lamda * f

    Output :
        hasil frekuensi gelombang dalam satuan Hz
        hasil cepat rambat gelombang dalam satuan m/s
'''

lamda = int(input("Masukan panjang gelombang (meter) = "))
n = int(input("Masukan jumlah gelombang = "))
t = int(input("Masukan waktu (sekon) = "))

f = (n/t)
V = (lamda * f)

print(f"Frekuensi gelombang adalah {f} Hz")
print(f"Cepat rambat gelombang adalah {V} m/s")