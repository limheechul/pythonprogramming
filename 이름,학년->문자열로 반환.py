def introduce(name, grade):
    first_name = name[1:]
    next_grade = grade + 1
    return f"{first_name}은 내년에 {next_grade}학년입니다."

name = input("이름? ")
grade = int(input("학년? "))

print(introduce(name, grade))
