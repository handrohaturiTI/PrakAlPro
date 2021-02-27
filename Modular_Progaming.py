# Handro Haturi
# 71200590
# Grub B
# Universitas Kristen Duta Wacana

# Modular Programing (fungsi)

"""
Seorang streamer Facebook bingung menghitung gaji bulanan dia dan bonus yang 
dia dapat. gaji dia adalah jumlah jam yg dia dapat perbulan di kali 15 dollar,
dan bonus dia 1 star = 0,01 dollar. hitunglah gaji bulanan dia dan star bonus 
dia kemudian jumlah kan. program ini di gunakan untuk streamer facebook saja 
dengan password facebook_gaming.


input : jumlah jam perbulan (whr) , jumlah star/bonus

proses : gaji = jam*(15*14000)
            bonus = (star*0.01)*14000

output : Gaji yang di dapat adalah Rp ......
            Bonus yang di dapat adalah Rp .....
            Jumlah total dari Gaji dan Bonus adalah Rp.....
"""
def gaji(jam):
    total_1 = jam*(15*14000)
    return total_1

def bonus(star) :
    total_2 = (star*0.01)*14000
    return total_2

a = str("facebook_gaming")
passw = input("Masukan password anda : ")
if passw == a :
    jam = int(input("Masukan jumlah jam perbulan (whr) : "))
    print(f"Gaji yang di dapat adalah Rp {gaji(jam)}")
    star = int(input("Masukan jumlah star/bonus anda : "))
    print(f"Bonus yang di dapat adalah Rp {bonus(star)}")
    jumlah_total = gaji(jam) + bonus(star)
    print(f"Jumlah total dari Gaji dan Bonus adalah Rp {jumlah_total}")
else :
    print("Password yang anda masukan salah!!!")



