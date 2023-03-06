arr = [1,2,3,4,5,6]

#enumerate 내장함수 이용해서 반복문돌기
x = (1, 2, 3)
a, b, c = x
for i, e in enumerate(arr):
    print(i, e) # x is tuple type ()