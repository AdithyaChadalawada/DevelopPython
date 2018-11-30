def range_div(a,b):
        finallist = []
        for i in range(a,b):
                if (i%7) == 0:
                        if i%5 != 0:
                                finallist.append(i)
        return finallist

finallist = range_div(2000,3000)
print finallist
