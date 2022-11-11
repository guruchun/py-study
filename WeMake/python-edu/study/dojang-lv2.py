# http://codingdojang.com/scode/350?answer_mode=hide
def p350():
    # s = 0
    # for i in range(1, 1000):
    #     if i%3 == 0 or i%5 == 0:
    #         s += i
    # print(s)
    print(sum(x for x in range(1, 1000) if x%3 == 0 or x%5 == 0))

# http://codingdojang.com/scode/393?answer_mode=hide
def p393():
    print(sum(str(x).count('8') for x in range(1,10001)))
    print("".join(str(i) for i in range(1,10001)).count('8'))
    print(str(list(range(1, 10001))).count('8'))

# http://codingdojang.com/scode/408?answer_mode=hide
def p408():
    S = [1, 3, 4, 8, 13, 17, 20]
    d = S[-1]
    plist = [S[i:i+2] for i in range(len(S)-1)]
    for p in plist:
        if p[1]-p[0] < d:
            d = p[1]-p[0]
            xy = p
    # print(p for p in plist if min(p[1]-p[0]))
    print(xy)



#####################################
if __name__ == "__main__":
    # p350()
    # p393()
    p408()
