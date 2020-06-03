def count():
    l = 0
    li = []
    while not (0 < l < 5000):
        words = input()
        li = words.split()
        l = len(li)
    N = len(li[-1])
    print(N)
    
if __name__ == "__main__":
    count()
