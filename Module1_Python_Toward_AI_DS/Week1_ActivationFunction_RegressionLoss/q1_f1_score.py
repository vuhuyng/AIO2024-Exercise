import math


def calc_f1_score(tp, fp, fn):
    if not isinstance(tp, int) or not isinstance(fp, int) or not isinstance(fn, int):
        if not isinstance(tp, int):
            print('tp must be int')
        if not isinstance(fp, int):
            print('fp must be int')
        if not isinstance(fn, int):
            print('fn must be int')
        return
    if (fp <= 0) or (tp <= 0) or (fn <= 0):
        print('tp and fp and fn must be greater than zero')
        return
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * ((precision * recall) / (precision + recall))
    return f1_score


assert math.isclose(round(calc_f1_score(tp=2, fp=3, fn=5), 2),
                    0.33, rel_tol=1e-09, abs_tol=1e-09)
print(round(calc_f1_score(tp=2, fp=4, fn=5), 2))
