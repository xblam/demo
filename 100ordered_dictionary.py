from collections import OrderedDict
from random import randint

benList = OrderedDict()

benList['jen'] = 'python'
benList['sarah'] = 'c'
benList['edward'] = 'ruby'
benList['phil'] = 'python'

# for i in benList:
#     print(i)
# for name, lang in benList.items():
#     print(f'{name.title()} is proficient in {lang}')

def dice6():
    return(randint(1,6))
def dice10():
    return(randint(1,10))

for i in range(10):
    print(dice6())
for i in range(10):
    print(dice10())




