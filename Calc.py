#/usr/bin/python

def add(x,y):
	return x+y

def sub(x,y):
	return x-y

def mul(x,y):
	return x*y

def div(x,y):
	return x%y

print "\n"
print "\tSELCT THE OPTIONS FROM THE BELOW"
print "\t\t1.Addition\n\t\t2.Subtraction\n\t\t3.Multiplication\n\t\t4.Division"

choice = int(input("Enter the choice :  "))

#print choice

num1 = float(input("Enter the number1 :  ")) 
num2 = float(input("Enter the number2 :  "))

if choice == 1:
	print "Result is : %s"%(add(num1,num2))

if choice == 2:
	print "Result is : %s"%(sub(num1,num2))

if choice == 3:
	print "Result is : %s"%(mul(num1,num2))

if choice == 4:
	print "Result is : %s"%(div(num1,num2))
