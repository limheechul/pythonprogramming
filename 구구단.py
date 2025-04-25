def input_p_number(prompt):
    n = 0
    while n <= 0:
        n = int(input(prompt))
    return n

def display_m_table(n):
    i = 1
    while i <= 9:
        print(f'{n} x {i} = {n * i:2d}')   #:2d는 숫자정렬
        i += 1

n = input_p_number('출력할 구구단을 양의 정수로 입력하세요: ')
display_m_table(n)
