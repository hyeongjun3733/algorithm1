import sys

while True:
    try:
        a, b = map(int, sys.stdin.readline().split())
        print(a + b)
    except:
        break
    
    # try, except, else, finally �������� ���� �Է°��� �߸��Ǿ� ������ �߻��ϴ� ��쿡 ����� �� �ִ�.