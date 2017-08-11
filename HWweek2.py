def subString(text):
	p1= 0
	p2 = 0
	sub = text[p1]
	cont = 0
	maxlsub = 1
	for x in range(1,len(text)):
		#print sub
		if text[x] in sub:
			if len(sub) > 1:
				p1 = sub.find(text[x]) + 1
				pass
			else:
				p1 = x
		else:
			sub = text[p1:x+1]
			cont = len(sub)
			maxlsub = max(maxlsub, cont)
		pass
	return maxlsub

filename = open('testHW2.txt')
lines = filename.readlines()
for line in lines:
	if line[-1] == '\n':
		line = line[:-1]
	print subString(str(line))
filename.close()
