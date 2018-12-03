import sys,math
c = int(50)
h = int(30)
d = raw_input("Enter value for d :")
d = d.split(',')
k = []
for i in d:
        k.append(str(int(round(math.sqrt(2*c*int(i)/h)))))


print k
