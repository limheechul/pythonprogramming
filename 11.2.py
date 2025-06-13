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
    @staticmethod
    def isvalid(h,m):
        if 0 <= h <= 23 and 0 <= m <= 59:
            return True
        else:
            return False
def main():
    t1 = Time(9)
    t2 = Time(9, 30)
    t1.display()
    t2.display()
    later = t1.add(Time(1, 15))
    later.display()
    if Time.isvalid(25, 0):
        print('유효한 시각')
    else:
        print('유효하지 않은 시각')
main()
