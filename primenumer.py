num = int(raw_input("Enter a number?"))
print num

#b = num/2


for i in range(2,num):
	if (num % i) == 0:
		print '%s is not a prime'%(num)
		break
else:
    print '%s is prime'%(num)
