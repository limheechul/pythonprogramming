def draw_line_string(msg):
    nstr = len(msg)
    rep_char('-', nstr * 2 + 4)
    print(f'  {msg}  ')
    rep_char('-', nstr * 2 + 4)

draw_line_string('안녕하세요')
draw_line_string('안녕')
