name = raw_input("whats the word ")

def reverse(x):
	value = ""
	for i in x:
		value = i + value
        return value


output = reverse(name)
print output
