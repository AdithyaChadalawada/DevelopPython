i = j = 0
while True:
	value = raw_input()
	if not value:
		break;
	else:
		a = value.split(' ')	
		if "D" in a:
			i += int(a[1])
		if "W" in a:
			j += int(a[1])

print i
print j

print "remaining amount is : %s"%(int(i) - int(j))	
