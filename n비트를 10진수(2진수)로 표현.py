def set_all_bits(n):
    return (1 << n) - 1

def get_integer(prompt):
    return int(input(prompt))

n = get_integer('설정할 비트 수는?')
all_ones = set_all_bits(n)
print(n, '비트를 모두 1로 설정한 수는', all_ones,'(',bin(all_ones), ')이다')
