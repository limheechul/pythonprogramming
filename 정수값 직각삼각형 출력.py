#왼쪽 기울도록 정수 나열
def display_triangle(height):
    for i in range(1, height + 1):
        for j in range(1, i+1):
            print(j, end='')
        print()

h = int(input('높이? '))
display_triangle(h)

#오른쪽 기울도록 * 나열
def display_triangle(height, ch = '*'):
    for i in range(1, height + 1):
        draw_line(' ', height - i)
        draw_line(ch, i)
        print()
    
def draw_line(ch, n):
    print(ch * n, end='')

h = int(input('높이? '))
display_triangle(h)
