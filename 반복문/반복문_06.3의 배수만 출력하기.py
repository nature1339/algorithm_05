arr = [123, 234, 345, 345, 345, 999]



# a = [ ]
# for i in arr: # 1, 2, 3, 4, 5, 6, 7
#     if i % 3 == 0:
#         a.append(i)

# print(a)

for i in range(len(arr)):
    if arr[i] % 3 == 0:
        print(arr[i])         
    