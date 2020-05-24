put_s = input()
count = 0
f_half, s_half = put_s[:len(put_s)//2], put_s[(len(put_s)+1)//2:]
if f_half == reversed(s_half):
    print(count)
else:
    for x in range(len(f_half)):
        if f_half[x] != s_half[len(s_half)-x-1]:
            count += 1
    print(count)