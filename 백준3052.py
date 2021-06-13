# num_list1 = []
# num_list2 = []

# for _ in range(10):
#     a = int(input())
#     num_list1.append(a)

# for i in num_list1:
#     b = i % 42
#     num_list2.append(b)

# num_list2.sort()
# comp = num_list2[0]

# for i in num_list2:
#     index = 1
#     if comp != i:
#         comp = i
#         index += 1
#     else:
#         continue

# print(index)

num_list = []
for _ in range(10):
    num_list.append(int(input()) % 42)

num_list = set(num_list)
print(len(num_list))