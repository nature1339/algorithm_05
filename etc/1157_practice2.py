words = input().upper() #zZa
unique_words = list(set(words))

cnt_list = [] # [z, a]

for x in unique_words :  # z a
    cnt = words.count(x)   #z
    cnt_list.append(cnt)    #[2, 1]

if cnt_list.count(max(cnt_list)) > 1: #
    print("?")

else :    
    max_index = cnt_list.index(max(cnt_list))
    print(unique_words[max_index])