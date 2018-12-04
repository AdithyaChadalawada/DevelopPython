def pwd_check():
        pwd= str(raw_input("Enter the password : "))
        if len(list(pwd)) < 5:
                print "please enter again"
        j = k = h = 0
        for i in list(pwd):
                if i.isupper():
                        h += 1
                if i.islower():
                        j += 1
                if i.isdigit():
                        k += 1
        if k < 1 or j < 1 or h < 1:
                print "please enter again: Value should contain at least 1 number/1 lowercase/1 uppercase"
                pwd_check()
        else:
                return pwd


final = pwd_check()
print final
~                    
