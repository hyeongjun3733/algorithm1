num_list = []

for _ in range(9):
    a = int(input())
    num_list.append(a)

n_max = max(num_list)

print(n_max)
print(num_list.index(n_max)+1)