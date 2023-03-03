# n = int(input())

# n_list = []
# temp = []
# for i in range(n):
#     n_list[] =+1
#     print(n_list(max))
    
words = input().upper() # MISSISSIPI  #리스트에서나 카운트에서도 리스트사용가능
unique_words = list(set(words)) #set


cnt_list = []
for x in unique_words : 
    cnt = words.count(x) #count 함수: 특정 요소가 그 안에 몇  개 있는지 세어준다.
    cnt_list.append(cnt) #append 함수: 리스트에 삽입한다.
# words = MISSISSIPI
# unique_words = [M,I,S,P]
 #cnt = words.count(M) # words 리스트에서 m 이 몇개냐 -> 1
#cnt_list.append(cnt) [1] 
# x = i
#cnt_list = [1, 4, 4, 1] 



# 1, 4, 4, 1
# 1 2 3 4

if cnt_list.count(max(cnt_list)) > 1 :  # max(cnt_list) = 4 
    #cnt_list.count(4) , -> 2
    print('?')
    #단어에서 가장 많이 사용된 알파벳 ->  I, S (4)
    #max(cnt_list) => rkw
    #max([1,4,4,1]) = 4
    #zZa 
    #unique list = [z, a] 
    #count list = [2, 1]
    #max(cnt_list) = 2
    #cont_list.index(max(cnt_list)) = 0
else :
    max_index = cnt_list.index(max(cnt_list)) #0 
    #index함수: 어떤 요소가 몇번 인덱스에 있는지 
    print(unique_words[max_index])  #Z