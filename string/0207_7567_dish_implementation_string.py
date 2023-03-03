s = input()
  #이전 dish와 같은방향이면 +5 다른방향이면 +10

result = 10

for i in range(1, len(s)): #0부터 len-1까지 roop    
    if s[i] == s[i - 1]:
        result += 5
    else: 
        result += 10

print(result)    