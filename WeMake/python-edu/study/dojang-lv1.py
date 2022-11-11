
# http://codingdojang.com/scode/539?answer_mode=hide
def p539_fn(n):
    # get d
    return sum(x for x in range(1, n//2+1) if n%x == 0)

def p539():
    N = int(input("input: "))
    l = list()
    for i in range(1, N+1):
        if i == p539_fn(i):
            l.append(i)
    print(l)


#####################################
if __name__ == "__main__":
    p539()
