# I = ceil(M / A)
# M : 저작권이 있는 멜로디의 개수 (integer)
# A : 앨범에 수록된 곡의 갯수

# 23.53 --> 24
# 23. 0000001 -> 24

# 24 = 올림(M / A ), minimum M?
# 23 = M / A
# 5/2 = 2.5

# # I 는 항상 integer이고 원래 수에서 올림한것이기 때문에, I - 1 < x <= I 인 x를 올림하면 항상 I 가 된다.
# # ex) I = 24, 23.0001 ~24를 올림하면 24

# # I - 1 / M / A 라고 할때, M을 조금만 크게 해줘도 소수점이 생기기 때문에 올림하면 I가 된다. 따라서,

# input: A, I, output: Minimum possible M
# I - 1 = M / A
# M = A(I - 1) + 1

A, I = map(int, input().split())
print(A * (I - 1)+ 1)
