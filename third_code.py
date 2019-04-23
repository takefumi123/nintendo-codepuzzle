from second_code import SimpleBars
from second_code import Bars

morse_mapper = {
    "iI":"A",
    "Iiii":"B",
    "IiIi":"C",
    "Iii":"D",
    "i":"E",
    "iiIi":"F",
    "IIi":"G",
    "iiii":"H",
    "ii":"I",
    "iIII":"J",
    "IiI":"K",
    "iIii":"L",
    "II":"M",
    "Ii":"N",
    "III":"O",
    "iIIi":"P",
    "IIiI":"Q",
    "iIi":"R",
    "iii":"S",
    "I":"T",
    "iiI":"U",
    "iiiI":"V",
    "iII":"W",
    "IiiI":"X",
    "IiII":"Y",
    "IIii":"Z"
}
morse_reverse_mapper = {v:k for k, v in morse_mapper.items()}

def decode_morse(s):
    data = s.split()
    result = ""
    for x in data:
        result = result + morse_mapper.get(x)
    return result

def encode_morse(c):
    return morse_reverse_mapper.get(c)

if __name__ == "__main__":
    bs = Bars("I    IT ii  i I   I i   i   I  T")
    for i in range(26):
        bs.next()

    print(decode_morse(str(bs)))
