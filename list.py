# Handro Haturi
# 71200590
# Universitas Kristen Duta Wacana

# list
"""
Danu seorang pencatat nomer rumah. Danu sedang bingung 
mengurutkan nomer rumah nya. dan danu mempunyai kewajiban 
di komplek 1 . maka angka depan rumah di komplek tersebut 
harus 1. maka saya akan membantu dani membuat program untuk
mengurutkan dan menemukan angka depan yang salah.


input :lis berisi nomer rumah yang danu berikan

proses : perulangan sebanyak panjang list dan berapa banyak 
nomer rumah.

output : Nomer tersebut sudah benar dan (.....) ini urutan 
nomer rumahnya. jika salah maka akan mengelurkan Nomer rumah
dengan angka depan ini harusnya tidak berada di komplek 1.

"""
nomer_rumah = [124,123,127,231,125,128]
nomer_rumah.sort()

tampung =[]

for i in nomer_rumah:
    a = str(i)
    for j in a :
        tampung.append(j)
        break

if j == tampung[0]:
    print(f"Ini adalah urutan nomer rumah yang sudah benar {nomer_rumah} dan berada di komplek 1")
else:
    print(f"Nomer rumah dengan angka depan {j} tidak seharusnya berada di komplek 1")
