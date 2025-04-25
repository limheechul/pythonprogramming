def input_age(prompt):
    n = int(input(prompt))
    if 0 <= n <= 120:
        return n
    else:
        return -1

def is_adult(age):
    if age >= 19:
        return True
    else:
        return False

age = input_age('나이? ')
if age >= 0:
    if is_adult(age):
        print('당신은 성인입니다.')
    else:
        print('당신은 성인이 아닙니다.')
else:
    print('오류: 유효하지 않은 나이가 입력되어 판별할 수 없습니다!')
