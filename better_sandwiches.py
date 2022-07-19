from country_city import printWord

def getList():
    orderList = list()
    while True:
        ingredient = input('what do you want on your sandwich?: ')
        if ingredient == 'q':
            break
        orderList.append(ingredient)
    print(orderList)
        
def arbitraryList(*toppings):
    for i in toppings:
        print(i)

# arbitraryList('one', 'two', 'three', 'four')

# arbitraryList('ben Lam')
# arbitraryList('other things', 'more things', 'these things')

def makeCar(model, manufacturor, **factors ):
    describe = dict()
    describe['model'] = model
    describe['company'] = manufacturor
    for i in factors:
        describe[i] = factors.get(i)
    print(describe)

makeCar('bmw', 'made by ford', ben = 'one', lam = 3, haos = 'six', kaitlin = 'mahahososo')

# test = {'ben lam': 1, 'haos':2, 'hoasooss': 5}
# for i in test:
#     print(i)
#     print(test.get(i))
# for i in test.items():
#     print(i)

printWord()
