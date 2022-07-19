orders =['pastrami' ,'ham', 'beef', 'chicken', 'vegetarian', 'vegan', 'pastrami', 'pastrami']
finished_orders = list()

print(orders)

print('the restaurant if out of pastrami')

for i in orders:
    if i == 'pastrami':
        continue
    print(f'making a {i} sandwich!')
    finished_orders.append(i)

print(finished_orders)

print()