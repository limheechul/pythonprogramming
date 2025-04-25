def print_m_table(start, end):
    for i in range(1,10):
        for dan in range(start, end + 1):
            print(f'{dan} x {i} = {dan * i:2d}', end = '\t')
        print()
    
print_m_table(2,5)
print()
print_m_table(6,9)
