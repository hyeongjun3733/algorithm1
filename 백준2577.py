a = int(input())
b = int(input())
c = int(input())

mul = str(a*b*c) # ������ �и��Ͽ� ����Ʈ�� ����� ���ؼ��� �ϴ� ���ڿ��� �ٲ۴�
num_list = list(map(int, mul))

for i in range(10):
    print(num_list.count(i))