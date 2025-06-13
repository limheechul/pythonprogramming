def buy(sbag):
    print('[구입]')
    item = input('상품명? ')

    if item == '':
        return False
    sbag.append(item)
    print(f'장바구니에 {item}가(이) 담겼습니다\n')

    return True

def show(sbag):
    print('\n>>> 장바구니 보기: ', end='')
    print(sbag)

def save_data(sbag):
    with open('shoppingbag.txt', 'w') as file:
        for item in sbag:
            file.write(item+'\n')

def load_data():
    with open('shoppingbag.txt', 'r') as file:
        for line in file:
            shopping_bag.append(line.strip())
shopping_bag = []
import os
if os.path.exists('shoppingbag.txt'):
    print('[파일 읽기]')
    load_data()
    show(shopping_bag)
while True:
    if buy(shopping_bag) == False:
        break
show(shopping_bag)
save_data(shopping_bag)
