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
    print(f'precision is {precision}')
    print(f'recall is {recall}')
    print(f'f1_score is {f1_score}')
    return f1_score


if __name__ == "__main__":
    calc_f1_score(tp=2, fp=3, fn=4)

    calc_f1_score(tp='a', fp=3, fn=4)
