def convert_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60
    print(f"{seconds} 초는 {hours} 시간 {minutes} 분 {remaining_seconds} 초이다.")

def get_integer(prompt):
    return int(input(prompt))

seconds = get_integer('변환하고자 하는 시간(초)?')
convert_time(seconds)

def set_all_bits(n):
    return (1 << n) - 1

def get_integer(prompt):
    return int(input(prompt))
