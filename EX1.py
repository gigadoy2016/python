def greeting(inputX):
    print(int(inputX) * 5)

def EX_1(hh,mm,ss):
    print(hh + ":"+mm+":"+ss)
    h = int(hh) *360
    m = int(mm) * 60
    sec = h + m + int(ss)
    print( sec )

if __name__ == '__main__':
    h = input()
    m = input()
    s = input()
    EX_1(h,m,s)