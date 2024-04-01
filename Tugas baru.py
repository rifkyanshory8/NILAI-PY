absen=int(input('masukkan nilai absen=',))
uts=int (input('masukkan nilai uts=',))
uas=int(input ('masukkan nilai uas=',))
standar=50
jumlah=absen +uts + uas
rata_rata=jumlah/3
print('jumlah nilai yang didapatkan adala=',jumlah)
print('nilai rata rata yg didapatkan adalah =',rata_rata)
if rata_rata > standar:
	print('lulus,dengan nilai rata rata=',rata_rata)
else:
	print('anda belum beruntung')
	
if rata_rata >=90:
	grade='A'
elif rata_rata >=80:
	grade='B'
elif rata_rata >=70:
	grade='C'
else:
	kategori='D'
print('kategori :', kategori)
