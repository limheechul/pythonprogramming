with open('readme.txt', 'r') as file:
    for i in range(3):
        line = file.readline()
        print(f'{i+1}: {line.strip()}')
