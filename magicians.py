magicians = ['ben', 'lam', 'kat', 'ngo', 'alex']

def printNames(ls):
    for i in ls:
        print(i)

def makeGreat(ls):
    greatList = list()
    for i in range(len(ls)):
        greatList.append(f'the great {ls[i]}')
    return(greatList)

printNames(magicians)
printNames(makeGreat(magicians))









