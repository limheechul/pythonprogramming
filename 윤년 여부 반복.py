def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

while True:
    year = int(input('윤년 여부를 확인할 연도는? '))
    print(f'{year}년은', end = ' ')
    if is_leap_year(year):
        print('윤년입니다.')
    else:
        print('평년입니다.')

    rep = input('다른 연도도 확인하겠습니까? ')
    if rep != 'y' and rep != 'Y':
        break
    print()
