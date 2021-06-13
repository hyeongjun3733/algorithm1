import sys

# N = int(input())

# num_list = list(map(int,sys.stdin.readline().split()))

# print(min(num_list), max(num_list), end=" ")

N = int(sys.stdin.readline())

num_list = list(map(int, sys.stdin.readline().split()))

for i in num_list:
    n_min = num_list[0]
    n_max = num_list[0]
    if i < n_min:
        n_min = i
    if i > n_max:
        n_max = i

print(n_min, n_max, end=" ")
        
    