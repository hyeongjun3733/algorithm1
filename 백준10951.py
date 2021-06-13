import sys

while True:
    try:
        a, b = map(int, sys.stdin.readline().split())
        print(a + b)
    except:
        break
    
    # try, except, else, finally 구문들을 통해 입력값이 잘못되어 오류가 발생하는 경우에 대비할 수 있다.