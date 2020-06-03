n = 1
ip = []
ma = []
l = [0, 0, 0, 0, 0, 0, 0] # a, b, c, d, e, wpm, pr
while n != 0:
    a = input().strip().split("~")
    n = len(a)
    if n == 1:
        break
    ipn = a[0].split(".")
    try:
        if 1 <= int(ipn[0]) <= 126:
            p = 0
        elif 128 <= int(ipn[0]) <= 191:
            p = 1
        elif 192 <= int(ipn[0]) <= 223:
            p = 2
        elif 224 <= int(ipn[0]) <= 239:
            p = 3
        elif 240 <= int(ipn(0)) <= 255:
            p = 4
        elif int(ipn[0]) == 0 or 127:
            continue
        if 0 <= int(ipn[1]) <= 255:
            if int(ipn[0]) == 10:
                n = 6
            elif int(ipn[0]) == 172 and 16 <= int(ipn[1]) <= 31:
                n = 6
            elif int(ipn[0]) == 192 and int(ipn[1]) == 168:
                n = 6
            if 0 <= int(ipn[2]) <= 255:
                if 0 <= int(ipn[3]) <= 255:
                    l[p] += 1
                    if n == 6:
                        l[n] += 1
                else:
                    l[5] += 1
                    continue
            else:
                l[5] += 1
                continue
        else:
            l[5] += 1
            continue
    except:
        l[5] += 1
        continue
    mn = a[1].split(".")
    b = ""
    for ms in mn:
        b += bin(int(ms))[2:]       
    le = b.find("0")
    ri = b.rfind("1")
    if le < ri:
        l[p] -= 1
        if n == 6:
            l[n] -= 1
        l[5] += 1
        n = 1

for o in l:
    print(str(o),end=" ")


n = 1

while n != 0:
    n = int(input())
    if n == 0:
        break
    cnt = 0
    while n > 0:
        if n == 1:
            break
        if n == 2:
            cnt += 1
            break
        cnt += n // 3
        n = n // 3 + n % 3
    print(cnt)

dic = {}
a = input().strip()
for c in a:
    if c not in dic:
        dic[c] = 1
    else:
        dic[c] += 1
        
val = sorted(dic.values())
va = val[0]
minword = []
for k, v in dic.items():
    if v == va:
        minword.append(k)

new = []
for w in a:
    if w not in minword:
        new.append(w)

print(''.join(new))