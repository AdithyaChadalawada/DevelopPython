def word_count(string):
        number = dict()
#       print "number is %s"%(number)
        line = string.split()

        for word in line:
                if word in number:
                        number[word] += 1
                else:
                        number[word] = 1

        return number


print word_count('adi adi adi is great')


def word_count(string):
                number={}
                line = string.split()
                for i in line:
                        count = line.count(i)
                        number[i] = count
                print number        
          return number



