#전공평점은 전공과목별 (학점 × 과목평점)의 합을 학점의 총합으로 나눈 값이다
rating = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
grade = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0]
total = 0 # 학점 총합을 담을 변수
result = 0 # (학점 * 과목평점) 총합을 담을 변수
for i in range(20): #20줄 입력
    s, p, g = input().split()
    #과목, 학점, 과목평점이 띄어쓰기로 구분되어 들어오므로 split을 사용해서 세 변수에 나눠 저장
    p = float(p) #실수 자료형으로 바꿔줌 (사칙연산 위해)
    if g != 'P' : # 등급이 P인 과목은 계산 안함
        total += p
        result += p * grade[rating.index(g)]
print('%.6f'%(result / total))
#result를 total로 나누면 평점이고, 소수점 아래 6자까지 출력하기 위해 '%.6f'%를 사용
