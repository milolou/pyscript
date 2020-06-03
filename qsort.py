def getin():
    n = 1
    li = []
    while n != 0:
        try:
            c = int(input())
            n = 0
        except:
            pass
    while n < c:
        num = input()
        try:
            rNum = int(num)
            li.append(rNum)
            n += 1
        except:
            pass
    return list(set(li))

    
def swap(l, i, j):
    c = l[i]
    l[i] = l[j]
    l[j] = c
    
def sort(l, n, m):
    N = m - n + 1
    if N < 2:
        return
    i = n + 1
    k = n
    mid = int(N / 2)
    swap(l, n, mid)
    while i <= m:
        if l[i] > l[n]:
            k += 1
            swap(l, i, k)
        i += 1
    swap(l, n, k)
    sort(l, n, k - 1)
    sort(l, k + 1, m)
    
if __name__ == "__main__":
    l = getin()
    sort(l, 0, len(l) - 1)
    for i in l:
        print(i)
