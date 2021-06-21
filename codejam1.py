# INF = 1e6
# test_cases = int(input());

# for i in range(1,test_cases+1):
#     x,y,input_string = input().split()
#     x,y = int(x),int(y)

#     last_c = 0
#     last_j = 0
#     n = len(input_string)
#     for j in range(n):
#         new_j = INF
#         new_c = INF
#         if(input_string[j] == '?'):
#             new_c = min(last_c,last_j+y)
#             new_j = min(last_j,last_c+x)
#         elif(input_string[j] == 'C'):
#             new_c = min(last_c,last_j+y)
#         elif(input_string[j] == 'J'):
#             new_j = min(last_j,last_c+x)
#         last_c = new_c
#         last_j = new_j
#     print(f'Case #{i}: {min(last_c,last_j)}')


