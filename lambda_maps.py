person ="subejo bejo bejos"
nambahdua = (lambda a : print(a + 2))
nambahdua(2)

harga_satu = [200, 300]
harga_dua = [800,1000]

hargaTermurah = map(min, harga_satu, harga_dua)
print(list(hargaTermurah))

hargaPertama = map(harga_satu, harga_dua)
print(list(hargaPertama))