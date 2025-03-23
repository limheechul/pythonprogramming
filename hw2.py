def get_integer():
    amount = int(input("동전으로 교환하고자 하는 금액은? "))
    return amount

def exchange(amount):
    coins = [500, 100, 50, 10]
    coin_counts = {}

    for coin in coins:
        coin_counts[coin] = amount // coin
        amount %= coin

    for coin in coins:
        print(coin,'원 동전의 개수:', coin_counts[coin])

amount = get_integer()
exchange(amount)
