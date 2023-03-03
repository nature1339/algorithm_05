arr = [1,2,3,4,5,6]

#반복문_04.짝수번째 숫자들만 출력하기

a = [ ]
for i in arr: # 1, 2, 3, 4, 5, 6, 7
    if i % 2 == 0:
        a.append(i)

print(a)
    