n = 1
ip = []
ma = []
l = [0, 0, 0, 0, 0, 0, 0] # a, b, c, d, e, wpm, pr
while n != 0:
    a = input().strip().split("~")
    n = len(a)
    if n == 1:
        break
    ip.append(a[0])
    ma.append(a[1])

for i in ip:
    ipn = i.split(".")
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
                p = 6
            elif int(ipn[0]) == 172 and 16 <= int(ipn[1]) <= 31:
                p = 6
            elif int(ipn[0]) == 192 and int(ipn[1]) == 168:
                p = 6
            if 0 <= int(ipn[2]) <= 255:
                if 0 <= int(ipn[3]) <= 255:
                    l[p] += 1
                else:
                    l[5] += 1
            else:
                l[5] += 1
        else:
            l[5] += 1
    except:
        l[5] += 1
    
for m in ma:
    mn = m.split(".")
    b = bin(int(''.join(mn)))
    le = b.find("0")
    ri = b.rfind("1")
    if le > ri:
        l[5] += 1

for o in l:
    print(str(o),end=" ")