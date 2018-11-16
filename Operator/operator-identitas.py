# Operator identitas adalah cara bagaimana kita mengenali suatu variabel di dalam memori di Python.
angka1 = 8
angka2 = 8
angka3 = "8"

print (angka1 is angka2) # is, untuk memeriksa apakah dua variabel memiliki isi dan tipe data yang sama
# id(), untuk mengetahui lokasi variabel / objek di memori walaupun isi dan tipe datanya sama
print (id(angka1) is id(angka2))
print (angka1 is not angka3) # is not, memastikan bahwa dua variabel tidaklah sama baik isi dan tipe datanya
print (angka1 is angka3)
