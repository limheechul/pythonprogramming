class Time:
    def __init__(self,h=0,m=0):
        self.h = h
        self.m = m
    def display(self):
        print(f'{self.h}:{self.m:02d}')
    def add(self,time):
        h = self.h + time.h
        m = self.m + time.m
        if m >= 60:
            m -= 60
            h += 1
        return Time(h,m)

    def tostring(self):
        return f'{self.h:02d}:{self.m:02d}'
    @staticmethod
    def isvalid(h,m):
        if 0 <= h <= 23 and 0 <= m <= 59:
            return True
        else:
            return False


from datetime import datetime
import pickle

def get_current_time():
    now = datetime.now()
    hour = now.hour
    minute = now.minute
    return Time(hour,minute)

def save_time(time):
    with open('last.dat','wb') as file:
        pickle.dump(get_current_time(),file)
def load_time():
    with open('last.dat','rb') as file:
        Time = pickle.load(file)
        return Time

import os
if os.path.exists('last.dat'):
    last = load_time()
    now_time = get_current_time()
    print(f'안녕하세요, 마지막으로 {last.tostring()}에 실행되었습니다.')
else:
    print('안녕하세요, 처음 실행되었습니다.')

now_time = get_current_time()
print(f'지금은 {now_time.tostring()} 입니다.')
save_time(now_time)
