
inst = open("instructions.txt", "r")

instructions = ['.']

for i in inst.read():
	if i == '-' or i == '.':
		instructions.append(i);

bits = []
current = 0

for i in range(len(instructions) - 2, -1, -1):
	if instructions[i] == '-':
		current += 1
	elif instructions[i] == '.':
		print(current)
		bits.append(current)
		current = 0

bits = sorted(bits)

length = 1
message = ""
symbol = 0

for i in range(len(bits)):
	if bits[i] > length * 8:
		length += 1
		message = chr(symbol) + message
		symbol = 0
	current = bits[i] % 8
	symbol = symbol | 2 ** (current - 1)

if symbol > 0:
	message = chr(symbol) + message
	
print(message)


