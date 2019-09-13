raw = open('.raw_giftcodes.txt', 'r')
target = open('.giftcodes', 'w')

ans = 0
cnt = 0

while(True):
    line = raw.readline()
    if not line:
        break
    if (cnt % 4 == 0):
        print(line, end='')
        target.write(line)
        ans += 1
    cnt += 1

print(ans)
