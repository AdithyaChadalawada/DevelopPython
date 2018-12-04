word = raw_input().split(',')
#print " ".join(set(word))
print word
l = []
[l.append(i) for i in word if i not in l]
print " ".join(l)
