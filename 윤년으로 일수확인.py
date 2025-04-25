def is_leap_year(y):
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        return True
    else:
        return False

def month_days(y,m):
    if m == 4 or m == 6 or m == 9 or m == 11:
        return 30

    elif m == 2:
        if is_leap_year(y):
            return 29
        else:
            return 28
    else:
        return 31

year = int(input('연도? '))
month = int(input('월? '))
ndays = month_days(year, month)
print(f'{year}년 {month}월은 {ndays}일까지 있습니다.')
