total_cost = int(input('구매한 물건의 총구매 금액은?'))
payment = int(input('고객으로부터 지불받은 금액은? '))
change = payment - total_cost

def show_change(amount):
    print('잔돈:',amount,'원')
    n5000 = amount // 5000
    amount %= 5000
    n1000 = amount // 1000
    print('>5000원권',n5000,'장')
    print('>1000원권',n1000,'장')

show_change(change)
