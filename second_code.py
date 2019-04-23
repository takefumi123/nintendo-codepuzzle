class SimpleBars():
    def __init__(self, string):
        self.s = list(string)

    def __setitem__(self, i, c):
        self.s[i] = c

    def __len__(self):
        return len(self.s)

    def __str__(self):
        return "".join(self.s)

    def next(self):
        answer = []

        answer.append(self._get_token(self.s[-1], self.s[0], self.s[1]))
        for i in range(1, len(self.s) - 1):
            answer.append(self._get_token(self.s[i - 1], self.s[i], self.s[i + 1]))
        answer.append(self._get_token(self.s[len(self.s) - 2], self.s[len(self.s) - 1], self.s[0]))

        self.s = answer
        return "".join(answer)

    def _get_token(self, a, b, c):
        print(a + " " + b + " " + c)
        if (a == "i") and (b == "T") and (c == "i"):
            return "i"
        elif (a == "i") and (b == "T"):
            return " "
        elif (b == "T") and (c == "i"):
            return " "
        elif (b == "T"):
            return "i"
        elif (a == "i") and (b == " ") and (c == "i"):
            return " "
        elif (a == "i") and (b == " "):
            return "i"
        elif (b == " ") and (c == "i"):
            return "i"
        elif (b == " "):
            return " "
        return "T"

class Bars(SimpleBars):
    def __init__(self, string):
        super(Bars, self).__init__(string)
        self.t = [{ " ":" ", "i":"T", "T":"i", "I":"I" }, { " ":"i", "i":"I", "T":" ", "I":"T" }];

    def _get_token(self, a, b, c):
        count = 0
        if (self._is_black(a)):
            count = count + 1
        if (self._is_black(c)):
            count = count + 1
        return self.t[count % 2][b]

    def _is_black(self, c):
        return (c == "i" or c == "I")

if __name__ == "__main__":
    import re
    bs = SimpleBars(' '*78)
    pos = 0; acc = 1; accx = 1; output = ""

    commands = "1(///(1iTiTiTi|||[(1 ])1( [L|[L|[L|[(] |1//)/)1i||1)///)1i\
    ||||1(///)1i(/////)1iTiTi[L!])|])[L!])])l|])1/( [(1/ ]L!l|[(1 ])1( //(1 ]L[L!|"

    for c in commands:
        if   c == "1": acc = 1
        elif c == "/": acc = acc * 2
        elif c == ")": pos += acc; pos %= len(bs)
        elif c == "(": pos -= acc; pos %= len(bs)
        elif c == "i" or c == "T" or c == " ":
            for i in range(acc):
                bs[pos] = c; pos += 1; pos %= len(bs)
        elif c == "]":
            s = str(bs)[pos:]+str(bs)[:pos+1];         m = re.search("^ *[iT]* ", s)
            acc = (m and m.end() - 1) or 0
        elif c == "[":
            t = str(bs); s = t[pos-1]+t[pos:]+t[:pos]; m = re.search(" [iT]* *$", s)
            acc = (m and len(s) - m.start() - 1) or 0
        elif c == "l": acc, accx = accx, acc
        elif c == "L": acc, accx = accx - acc, accx + acc
        elif c == "|": print(bs); bs.next()
        elif c == "!": output += chr((ord('0') + acc) % 128)

    print("answer: " + output)
