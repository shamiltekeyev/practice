# Введите число, и программа сгенерирует последовательность Фибоначчи
# до этого числа или до N-го числа.

def up_to_number(input_num):
    fib_nums = [0, 1]
    if input_num > 1:
        while fib_nums[-1] < input_num:
            next_num = fib_nums[-2] + fib_nums[-1]
            fib_nums.append(next_num)
        return fib_nums [:-1]
    elif input_num == 1:
        return fib_nums
    else:
        return 'Необходимо ввести натуральное число!'


if __name__ == '__main__':
    try:
        print(up_to_number(int(input('Введите натуральное число: '))))
    except ValueError:
        print('Необходимо ввести натуральное число!')
