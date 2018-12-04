i = raw_input()
d = {"UPPER":0,"LOWER":0,"DIGIT":0,"alpha":0}
for j in i:
	if j.isdigit():
		d["DIGIT"]+=1
	if j.isalpha():
		d["alpha"]+=1

	if j.isupper():
		d["UPPER"]+=1
	if j.islower():
		d["LOWER"]+=1

print d
