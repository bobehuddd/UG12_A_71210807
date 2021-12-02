tingginya = int(input("Input: "))

print("Output: ")
if tingginya == 0:
	print(" ")
elif tingginya < 0:
	print("maaf input salah ")
elif tingginya == 2:
	print(" * ")
	print("* *")
elif tingginya == 1:
	print("*")
else:
	print(" "*(tingginya-1)+"*"+" "*(tingginya-1))
	for bx in range (1,tingginya):
		print(" "*(tingginya-1-bx) + "*" + " "*(bx*2-1) +"*"+ " "*(tingginya-1-bx))
		if bx == tingginya-2:
			break
	for by in range(tingginya):
		print("*",end=' ' )