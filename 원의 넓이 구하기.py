#방법 1
def get_circle_area(radius):
    area = 3.14 * radius * radius
    return area
def get_radius(prompt):
    r = int(input(prompt))
    return r
r = get_radius('넓이를 구하고자 하는 원의 반지름은?')
res = get_circle_area(r)
print(f'반지름 {r}인 원의 넓이 = 3.14 * {r} * {r} = {res}')

#방법 2
def get_circle_area(radius):
    area = 3.14 * radius ** 2
    return area

radius = float(input('넓이를 구할 원의 반지름은? '))
area = get_circle_area(radius)
print(area)

# 방법 3
def get_circle_area():
    result = 3.14 * r ** 2
    return result

r = float(input('넓이를 구할 원의 반지름은?'))
area = get_circle_area()
print(area)
