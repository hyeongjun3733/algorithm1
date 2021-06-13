# N = int(input())
# index = 0

# while True:
#     if N < 10:
#         N = "0" + str(N)     
#     else:
#         N = str(N)
#     X = int(N[0]) + int(N[1]) 
#     if X < 10:
#         X = "0"+ str(X)
#     else:
#         X = str(X)
#     Y = N[1] + X[1]
#     index += 1
#     if N == Y:
#         break
#     else:
#         N = Y

# print(index)

N = int(input())
check = N
index = 0

while True:
    X = N//10 + N%10
    Y = 10*(N%10) + X%10
    index += 1
    N = Y
    if Y == check:
        break
    
print(index)