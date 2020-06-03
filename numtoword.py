l = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", \
     "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
while True:
    try:
        a = input().strip()
        b = []
        for i in a:
            if i.isalpha():
                b.append(i)
        c = []
        for j in l:
            for x in b:
                if x.lower() == j:
                    c.append(x)
        n = []
        cnt = 0
        for h in range(len(a)):
            if a[h].isalpha():
                n.append(c[cnt])
                cnt += 1
            else:
                n.append(a[h])
        print("".join(n))
    except:
        break

tb1 = {'1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', \
       '7':'seven', '8':'eight','9':'nine', '10':'ten', '11':'eleven', '12':'twelve',\
       '13':'thirteen', '14':'fourteen', '15':'fifteen', '16':'sixteen', \
       '17':'seventeen', '18':'eighteen', '19':'nineteen'}
tb2 = {'2':'twenty', '3':'thirty', '4':'forty', '5':'fifty', '6':'sixty', \
       '7':'seventy', '8':'eighty', '9':'ninety'}
while True:
    try:
        a = input().strip()
        l = len(a)
        if 3 < l <= 6:
            a = a[0:l-3] + ',' + a[-3:]
        elif 6 < l <= 9:
            a = a[0:l-6] + ',' + a[-6:-3] + ',' + a[-3:]
        else:
            a = a
        a = a[::-1]
        word = []
        s = 0
        dot = 0
        l = len(a)
        for c in range(l):
            if a[c] == '0':
                if c < l -1 and a[c+1] == '1':
                    word.append(tb1[a[c:c+2][::-1]])
                s += 1
                continue
            elif s == 0 and c < l - 1 and a[c+1] != '1':
                word.append(tb1[a[c]])
                s = 1
            elif s == 0 and c < l - 1 and a[c+1] == '1':
                word.append(tb1[a[c:c+2][::-1]])
                s = 1
            elif s == 0 and c == l - 1:
                word.append(tb1[a[c]])
                s = 1
            elif s == 1 and a[c] == '1':
                s = 2
                continue
            elif s == 1 and a[c] != '1':
                word.append(tb2[a[c]])
                s = 2
            elif s == 2:
                word.append('and')
                word.append('hundred')
                word.append(tb1[a[c]])
                s = 3
            elif s == 3 and dot == 0:
                word.append('thousand')
                s = 0
                dot = 1
            elif s == 3 and dot == 1:
                word.append('million')
                s = 0
        word = ' '.join(word[::-1])
        print(word)
    except:
        break