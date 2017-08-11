def wordBreak(text, dictionary):
	if text != '' and dictionary != {}:
		text = text.lower()
		for x in dictionary:
			if x.lower() in text:
				text = text.replace(x.lower(),'')
		if text == '':
			return True
	return False


#test
print wordBreak('youenjoy',{'pear', 'salmon', 'foot', 'prints', 'footprints', 'leave', 'you', 'sun', 'girl', 'enjoy' })
print wordBreak('youleavefootprints',{'pear', 'salmon', 'foot', 'prints', 'footprints', 'leave', 'you', 'sun', 'girl', 'enjoy'})
print wordBreak('salmonenjoyapples',{'pear', 'salmon', 'foot', 'prints', 'footprints', 'leave', 'you', 'sun', 'girl', 'enjoy'})
print wordBreak('youenjoy', {})
print wordBreak('',{ 'pear', 'salmon', 'foot', 'prints', 'footprints', 'leave', 'you', 'sun', 'girl', 'enjoy' })
print wordBreak('ThatboyTravel', {'hello', 'Salmon', 'foot', 'that', 'World', 'boy', 'travel'})

