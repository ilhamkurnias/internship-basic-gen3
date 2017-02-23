class BigRandom:
	def __init__(self):
		self.data = "data.txt"
		# add attributes if you need more
	def answer(self):
		noh = 0
		suc = 0 
		data = open('data.txt','r')
		#d = data
		for text in data.readline():
			idx = 0
			if text == "#":
				noh += 1
			noh = noh -1
		print(noh)		
				
		
		#return (noh,suc)
		# add methods if you need more
		
