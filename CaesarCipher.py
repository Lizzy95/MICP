#Norma Elizabeth Morales Cruz

def Caesar(pos, text):
	if pos < -1000000000 or pos > 1000000000:
		return "Error the shift number is out of range"
	newText = ''
	for x in range(0,len(text)):
		newChar = ord(text[x]) + pos
		if text[x] == ' ':
			newText += text[x]
		elif ord(text[x]) < 123 and ord(text[x]) > 96:
			if newChar < 97:
				newText += chr(122-(96-newChar))
			elif newChar > 122:
				newText += chr(97+(newChar-123))
			else:
				newText += chr(newChar)	
		elif ord(text[x]) < 91 and ord(text[x]) > 66:
			if newChar < 65:
				newText += chr(90-(66-newChar))
			elif newChar > 90:
				newText += chr(65+(newChar-91))
			else:
				newText += chr(newChar)	
		elif ord(text[x]) < 58 and ord(text[x]) > 49:
			if newChar < 48:
				newText += chr(57-(49-newChar))
			elif newChar > 57:
				newText += chr(48+(newChar-58))
			else:
				newText += chr(newChar)
	return newText

filename = open('test.txt')
lines = filename.readlines()
for line in lines:
	if line[-1] == '\n':
		line = line[:-1]
	textCase = line.split(':')
	print Caesar(int(textCase[0]), textCase[1])
filename.close()
