import math
import random


def regression_loss_func(num_sample, loss_name):
    if not num_sample.isdigit():
        print('number of sample must be an integer number')
        return
    num_sample = int(num_sample)

    if loss_name not in ['MAE', 'MSE', 'RMSE']:
        print(f'{loss_name} is not supported')
        return

    sum_loss = 0
    for i in range(num_sample):
        predict = random.uniform(0, 10)
        target = random.uniform(0, 10)

        if loss_name == 'RMSE' or loss_name == 'MSE':
            loss = (target - predict) ** 2
            print(
                f'loss name: {loss_name}, sample: {i}, pred: {predict}, target: {target}')
            print(f'    loss: {loss}')
            sum_loss += loss

        elif loss_name == 'MAE':
            loss = abs((target - predict))
            print(
                f'loss name: {loss_name}, sample: {i}, pred: {predict}, target: {target}')
            print(f'    loss: {loss}')
            sum_loss += loss

    if loss_name == "RMSE":
        final_loss = math.sqrt((1 / num_sample) * sum_loss)
        print(f'final {loss_name}: {final_loss}')
        return final_loss

    elif loss_name == "MAE":
        final_loss = (1 / num_sample) * sum_loss
        print(f'final {loss_name}: {final_loss}')
        return final_loss

    if loss_name == "MSE":
        final_loss = (1 / num_sample) * sum_loss
        print(f'final {loss_name}: {final_loss}')
        return final_loss


if __name__ == "__main__":
    n_sample = (
        input('Input number of samples (integer number) which are generated: '))
    loss_name = input('Input loss name: ')

    print(regression_loss_func(n_sample, loss_name))
