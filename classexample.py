class stringsclass(object):
	def __init__(self):
		self.s=""
	def get_string(self):
		self.s = raw_input("Enter the Strings :")
	def print_string(self):
		print self.s

str1 = stringsclass()
str1.get_string()
str1.print_string()
