i = raw_input().split(',')
k = []
#print(i[0],i[1])

for j in range(int(i[0]),int(i[1])):
        j = str(j)
        if (int(j[0])%2==0) and (int(j[1])%2==0):
                k.append(j)

print k
