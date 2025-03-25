def get_fixed_price(dt_rate, dd_price):
    o_price = dd_price / (1 - dt_rate / 100)
    return int(o_price)

dt_rate = int(input("할인율은? "))

a_dd_price = int(input("A 상품의 할인된 가격은? "))
a_o_price = get_fixed_price(dt_rate, a_dd_price)

b_dd_price = int(input("B 상품의 할인된 가격은? "))
b_o_price = get_fixed_price(dt_rate, b_dd_price)

print('A 상품의 정가는', a_o_price, '원')
print('B 상품의 정가는', b_o_price, '원')
