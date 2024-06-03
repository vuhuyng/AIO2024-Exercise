import math
def calc_f1_score(tp, fp, fn):
    if type(tp) != int or type(fp) != int or type(fn) != int:
        if type(tp) != int:
            print('tp must be int')
        if type(fp) != int:
            print('fp must be int')
        if type(fn) != int:
            print('fn must be int')
        return
    if fp <= 0 or fp <= 0 or fn <= 0:
        print('tp and fp and fn must be greater than zero')
        return
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * ((precision * recall) / (precision + recall))
    return f1_score


assert round(calc_f1_score(tp=2, fp=3, fn=5), 2) == 0.33
print(round(calc_f1_score(tp=2, fp=4, fn=5), 2))
