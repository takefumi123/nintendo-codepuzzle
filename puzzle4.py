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

bs = Bars("ITT TI I T TIii")
before = str(bs)
for i in range(100):
    bs.next()
    if str(bs) == "ITT TI I T TIii":
        #出力"iiI Ii I i Ii"をモールス信号で変換すると答えはUNTEN
        print(before)
    before = str(bs)
