age = int(input('당신의 나이는? '))
res = 0 <= age <= 120
print(f'{age}은(는) 유효한 나이인가? {res}')

res = age < 0 or age > 120
print(f'{age}은(는) 유효한 나이가 아닌가? {res}')
print(f'{age}은(는) 유효한 나이인가? {not res}')
