from second_code import SimpleBars
from third_code import Bars
from third_code import decode_morse

if __name__ == "__main__":
    bs = Bars("ITT TI I T TIii")
    before = str(bs)
    for i in range(100):
        bs.next()
        if str(bs) == "ITT TI I T TIii":
            print(decode_morse(before))
            break
        before = str(bs)
