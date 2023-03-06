# 풀이 1.
s = input() #level
chk = 1
#chk 초깃값은 1
for i in range(len(s)//2): # 몫 2
#단어 길이의 반으로 탐색 범위 설정
    if s[i] != s[len(s)-i-1]: #1234321 동일하지 않으면 chk = 0  비교연산자아님
    #단어의 양 끝을 조여가며 일치하는지 비교 (10글자면 1,10비교->2,9비교...)
        chk = 0
        break
   #일치하지 않으면 0으로 바꿔주고 break
print(chk)
#최종적으로 양 끝이 모두 일치했으면 1, 아니면 0

# 풀이 2. (slicing = 문자열[start:end:step])
# word = input()
#word = "1234321"
# rev = word[::-1] # ==거꾸로된수 1234321 slicing해서 거꾸로 만들고
# if rev == word: #비교 word원래 처음거랑 거꾸로 된 변수 rev 비교
#     print(1)
# else:
#     print(0)