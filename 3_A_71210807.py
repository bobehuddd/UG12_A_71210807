kata_input = input("Input: ")
bx = 0
by = 0
print("Output:")
while by < len(kata_input):
	print(kata_input[0:by])
	by += 1
while bx < len(kata_input):
	print(kata_input[0:len(kata_input)-bx])
	bx += 1