import math

def is_number(n):
    try:
        float(n)   
        return True 
    except ValueError:
        return False

def calc_activation_func(x, act_name):
    if not is_number(x):
        print('x must be a number')
        return
    elif act_name not in ['sigmoid', 'relu', 'elu']:
        print(f'{act_name} is not supported')
        return
    else:
        x = float(x)

        if act_name == 'sigmoid':
            return 1 / (1 + math.exp(-x))
        elif act_name == 'relu':
            return max(0, x)
        elif act_name == 'elu':
            alpha = 0.01
            return x if x > 0 else alpha * (math.exp(x) - 1)

if __name__ == "__main__":
    x = input('Input x = ')
    act_name = input('Input activation function (sigmoid|relu|elu): ')

    result = calc_activation_func(x, act_name)
    if result is not None:
        print(f"{act_name} f({x}) = {result}")
