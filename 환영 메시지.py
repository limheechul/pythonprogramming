def draw_line_string(n):
    msg1 = 'hello' + n
    msg2 = "Welcome to seoul."
    nstr = len(msg1) if (len(msg1) > len(msg2)) else len(msg2)
    print('-'*nstr)
    print('Hello', n+',\n'+msg2)
    print('-'*nstr)

draw_line_string(input('input his/her name:'))
