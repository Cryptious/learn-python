# elif singkatan dari else if, yaitu kondisi lain yang ingin diuji, atau pengujian secara bercabang
# contohnya sebagai berikut

nilai = 90
if nilai > 80: #jika nilai lebih besar dari 80, maka
	print ("Selamat, kamu dapat nilai A") # mendapatkan nilai A
elif nilai > 70 and nilai <=80: # jika nilai 71 - 80, maka
	print ("Selamat, kamu dapat nilai B") #mendapatkan nilai B
elif nilai > 60 and nilai <=70: # jika nilai 61 - 70, maka
	print ("Selamat, kamu dapat nilai C") # mendapatkan nilai C
elif nilai > 45 and nilai <=60: # Jika nilai 46 - 60, maka
	print ("Selamat, kamu dapat nilai D") # mendapatkan Nilai D
else: # kondisi lain jika kondisi diatas tidak terpenuhi
	print ("Maaf, kamu dapat nilai E. Kamu harus ikut ujian remedial :(")

# silahkan ganti nilai Variabel dengan 75, 65, 50, atau dengan angka mu sendiri 
# selamat mencoba
