a = int(input())
b = int(input())
c = int(input())

mul = str(a*b*c) # 각각을 분리하여 리스트로 만들기 위해서는 일단 문자열로 바꾼다
num_list = list(map(int, mul))

for i in range(10):
    print(num_list.count(i))