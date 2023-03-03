arr = [1,2,3,4,5,6]

#반복문_04.홀수번째 숫자들만 출력하기

a = [ ]
for i in arr: # 1, 2, 3, 4, 5, 6, 7
    if i % 2 == 1:
        a.append(i)

print(a)
    