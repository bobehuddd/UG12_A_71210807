xyz = []
urutan_kursi = []
while True:
	nama_xyz = (input("Masukkan peserta: "))
	if nama_xyz == "STOP":
		break
	else:
		kursi = (input("Masukkan nomor kursi "+nama_xyz+": "))
	
	if kursi in urutan_kursi:
		print("Mohon maaf, kursi tersebut telah terisi")
	else:
		xyz.append(nama_xyz)
		urutan_kursi.append(kursi)
		
print("\nLihat kursi yang telah terisi: ")

for i in range(len(urutan_kursi)):
	print("Kursi nomor",urutan_kursi[i],"telah diisi oleh", xyz[i])