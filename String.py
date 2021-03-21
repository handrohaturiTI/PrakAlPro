# Handro Haturi
# 71200590
# Universitas Kristen Duta Wacana

# String

"""
saya mempunyai teman jurusan Hukum dan dia ingin membuat sebuah program sesuai 
yang ia butuhkan. semisal dia menginput katanya kemudian dia menginput huruf 
vokal yang ingin dia ganti a maka huruf vokal yang ada di kata tsb akan di ganti a
, jika i maka akan di ganti i semua dst. kemudian vokal tsb di buat huruf kapital 
agar dia mudah mngecek nya. dan saat menginput kata, kata tsb di kapital semua.

input : masukan kata , plihan huruf yang ingin di gantikan semua

proses : huruf vokal di ganti a semua, huruf vokal di ganti i semua, huruf vokal di 
        ganti u semua, huruf vokal di ganti e semua, huruf vokal di ganti o semua.

output: semua vokal sudah di ganti sesuai apa yang ingin user ganti.

"""

kata = input("Masukan kata: ").upper()
ganti = input(f"Kata anda adalah {kata} dan huruf vokalnya ingin di ganti dengan : ")

ganti1 = "a,i,u,e,o"

if ganti == "a":
    kata = kata.lower()
    for i in (kata):
        if i in ganti1 :
            i = "a"
            i = i.upper()
            print(i,end="")
        else:
            print(i,end="")
elif ganti == "i":
    kata = kata.lower()
    for i in (kata):
        if i in ganti1 :
            i = "i"
            i = i.upper()
            print(i,end="")
        else:
            print(i,end="")
elif ganti == "u":
    kata = kata.lower()
    for i in (kata):
        if i in ganti1 :
            i = "u"
            i = i.upper()
            print(i,end="")
        else:
            print(i,end="")
elif ganti == "e":
    kata = kata.lower()
    for i in (kata):
        if i in ganti1 :
            i = "e"
            i = i.upper()
            print(i,end="")
        else:
            print(i,end="")
elif ganti == "o":
    kata = kata.lower()
    for i in (kata):
        if i in ganti1 :
            i = "o"
            i = i.upper()
            print(i,end="")
        else:
            print(i,end="")
else :
    print("Bukan huruf Vokal")
