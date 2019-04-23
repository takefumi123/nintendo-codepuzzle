from third_code import decode_morse

def take_away_T(s):
    return s.replace("T", "")

if __name__ == "__main__":
    #take away T : 変換前後の合計2回Tを省く。
    #take away br : 改行を省いて各行を連結する。
    result = take_away_T(decode_morse(take_away_T("iiI Ii I i Ii"))) \
           + take_away_T(decode_morse(take_away_T("ITT TI I T TIii"))) \
           + take_away_T(decode_morse(take_away_T("T i  I Iii  TTT")))
    print(result)
