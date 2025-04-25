#정삼각형
a = 8
for i in range(a):
    print(' ' * ((a - 1) - i), end = '')
    print('*' * (2 * i + 1))

#마름모
a = 11
for i in range(a//2):
    print(' ' * (a//2 - i), end = '')
    print('*' * (2*i+1))

for i in range(a//2-1):
    print(' ' * (i + 2), end = '')
    print('*' * ((a//2*2)-3-2*i))

#모래시계
a = 8

for i in range(a-1):
    if a // 2 > i:
        print(" " * i, end="")
        print("*" * (a - 2 * i - 1))
    else:
        print(" " * (a - i - 2), end="")
        print("*" * ((2 * i) - a//2 - 1))

  #트리플 삼각형
  a = 8
for i in range(a):
    if i < (a//2):
        for x in range(a-i):
            print(" ", end="")
        for x in range(i*2+1):
            print("*", end="")
    else:
        for x in range(a - i):
            print(" ", end="")
        for x in range(i*2+1 - a):
            print("*", end="")
        for x in range(a - (i*2+1 - a)):
            print(" ", end="")
        for x in range(i*2+1 - a):
            print("*", end="")
    print()

#거꾸로 계단 왼쪽
n = int(input())
star = '*'

for i in range(n , 0, -1): # n부터 1까지 1씩 감소하면서 반복
    print(i * star)
n = int(input())

for i in range(n,0,-1): #n~1까지 내림차순 순서대로 반복
    print("*"*i) #5입력 시 별다섯개

#거꾸로 계단 오른쪽
n = int(input())
star = '*'
blank = ' '

for i in range(0, n): #0부터 n-1까지 순서대로
    print(blank * i + star * (n - i)) #공백을 순서대로 0부터~n-1까지 
n = int(input())

for i in range(n, 0, -1): #내림차순 n~1까지
   print(" "*(n-i)+"*"*(i)) #5입력 시 5-5=0공백+5별

#거꾸로 세모
n = int(input())
for i in range(n,0,-1): #n~1 범위 내 순서대로 내림차순 반복
    print(" "*(n-i)+"*"*(i*2-1)) #5넣었을 때 5-5=0공백, 9별
n = int(input())
for i in range(n,0,-1): #n~1 내림차순
    print(" "*(n-i)+"*"*(i*2-1)) #5입력 시 공백 없고 + 별9
