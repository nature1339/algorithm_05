words = input().upper
unique_words = list(set(words))

cnt_list = []

for x in unique_words : # Mississipi #[M, I, S, P]
    cnt = words.count(x) #특정요소 x가  words 리스트안에 몇개있는지 세어준다. 
    cnt_list.append(cnt)  #cnt 요소를 cnt_list에 append한다.

if cnt_list.count(max(cnt_list)) > 1:
    print("?")
#가장큰 요소가 1개 이상이면(최대값이2개이상이면) ? 출력이고
# else 이면 그 요소 알파벳 출력

else :
    max_index = cnt_list.index(max(cnt_list))#cnt_list의 최대값이 cnt_list에서 몇번째 있는지
    #cnt_list의 최대값은 4 가 몇번째 있는지는 0번째 /최대값이 몇번째요소인지
    print(unique_words[max_index]) # unique_words리스트에서 그요소출력
    #unique_words 리스트에서 최대값
    #