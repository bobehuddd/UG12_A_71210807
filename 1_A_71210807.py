Bx_6=input("Masukkan deret angka : ")
Cy_6=Bx_6.split(",")
totalnya=0
bil=''
for o in Cy_6:
    if int(o)%2==0:
        number=0+int(o)
    else:
        number=0-int(o)
    totalnya=totalnya+number
print("Total: ",end='')
for o in Cy_6:
    if int(o)%2==0:
        operats_6=("+ "+str(o)+" ")
    else:
        operats_6=("- "+str(o)+" ")
    bil+=operats_6
if bil[0]=="+":
    print(bil[2:len(bil)])
else:
    print(bil)
print("Hasil perhitungan di atas ialah: ",totalnya)