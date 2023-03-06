#counting sort, 한국어로 계수 정렬이라고 함. 시간복잡도는 가장 빠르지만 ,메모리 문제로 정렬할 수가 작을 때만 사용가능한 정렬.
import sys #sys 는 라이브러리 /시간초과를 막기 위해
n = int(sys.stdin.readline()) #더 빠른 입력문 사용
num_list = [0]*10001 #0으로 초기화된 길이 10001짜리 리스트
for i in range(n): #n = 10 i = 0 1 2 3 4 5 6 7 8 9
    num_list[int(sys.stdin.readline())] += 1 #count해줌
                 #input  num_list[5] += 1

for i in range(1, 10001): #1부터 10000까지 순서대로 출력하므로 자연스럽게 정렬됨
    if num_list[i] != 0: 
        for j in range(num_list[i]): #count해준만큼 출력
            print(i)