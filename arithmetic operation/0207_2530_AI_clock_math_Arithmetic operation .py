h, m, s = map(int, input().split())
extra_sec = int(input())

total_sec = h * 3600 + m * 60 + s + extra_sec
h = total_sec // 3600
total_sec -= (h * 3600)

m = total_sec // 60
total_sec -= (m * 60)

s = total_sec

h %= 24
print("{} {} {}".format(h, m, s))

#second -> minute, hour