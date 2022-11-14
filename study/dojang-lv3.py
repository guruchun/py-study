# http://codingdojang.com/scode/266
def p266():
    X, Y = (int(x) for x in input("input 2 number: ").split(" "))
    matrix = [[-1 for i in range(Y)] for j in range(X)]

    x = y = 0
    dx = 0
    dy = 1
    seq = 0
    while matrix[x][y] == -1:
        matrix[x][y] = seq
        seq += 1

        x, y = x+dx, y+dy
        if x in [-1, X] or y in [-1, Y] or matrix[x][y] != -1:
            x, y = x - dx, y - dy # prev xy
            dx, dy = dy, -dx      # new clock-wise
            x, y = x+dx, y+dy     # new xy

    for a in matrix:
        print(a)


# http://codingdojang.com/scode/314
def p314():
    #     top   up-l,r mid dn-l,r bottom
    d = {0:["-", "||", " ", "||", "-"],
         1:[" ", " |", " ", " |", " "],
         2:["-", " |", "-", "| ", "-"],
         3:["-", " |", "-", " |", "-"],
         4:[" ", "||", "-", " |", " "],
         5:["-", "| ", "-", " |", "-"],
         6:["-", "| ", "-", "||", "-"],
         7:["-", " |", " ", " |", " "],
         8:["-", "||", "-", "||", "-"],
         9:["-", " |", "-", " |", "-"]}

    s, n = input().split()
    while s != "0" and n != "0":
        size = int(s)
        nums = [int(x) for x in n]
        for r in range(2*size+3):
            line = ""
            for n in nums:
                if r == 0:
                    line += (" " + d[n][0]*size + " " )
                elif r < size+1:
                    line += (d[n][1][0] + " "*size + d[n][1][1] )
                elif r == size+1:
                    line += (" " + d[n][2]*size + " " )
                elif r < 2*size+2:
                    line += (d[n][3][0] + " "*size + d[n][3][1] )
                else:
                    line += (" " + d[n][4]*size + " " )
                line += " "
            print(line)
        s, n = input().split()


# http://codingdojang.com/scode/327
import regex as re
def p327_slurpy(s):
    global re_slimp
    m = re_slimp.match(s)
    if m:
        m2 = re_slump.match(m.remains)
        if m2: return True
        else: return False
    else:
        return  False

def p327():
    global re_slump, re_slimp
    # slump - (D or E) and F+ and (slump or G)
    slump_pattern = "([D|E]F+)+G"
    re_slump = re.compile(slump_pattern)
    # slimp - A and (H or ((B and slimp and C) or (slump and C))
    slimp_pattern = "AH|A([D|E]F+)+GC|AB(?R)C"
    re_slimp = re.compile(slimp_pattern)

    n = int(input())
    instr = [input() for n in range(0, n)]
    print("SLURPYS OUTPUT")
    for s in instr:
        if p_327_slurpy(s):
            print("YES")
        else:
            print("NO")
    print("END OF OUTPUT")


# http://codingdojang.com/scode/365
def p365_fn(n):
    return n + sum(int(x) for x in str(n))

def p365():
    d_list = set()
    for i in range(1,5000):
        d_list.add(p365_fn(i))

    n_list = set(range(1,5000))
    print(sum(n_list-d_list))


#####################################
if __name__ == "__main__":
    # p266()
    # p314()
    p327()
    # p365()
