def lets_tea_break(m, e, n, c):
    if pow(m, e) % n == c:
        return str(m)
    return ""

def output(x):
    answer = lets_tea_break(*[int(i) for i in (x, 1985, 33067, 84)])
    if answer != "":
        print("http://cp1.nintendo.co.jp/" + answer)

if __name__ == "__main__":
    for i in range(100000):
        output(i)
