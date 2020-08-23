# Calculator


def get_operation():
    signs = ['+', '-', '*', '/', 'q']
    while True:
        sign = input('Operation sign: ')
        if sign not in signs:
            print('Correct signs: "+", "-", "*", "/" or "q" to exit.')
            continue
        elif sign == 'q':
            exit()
        else:
            try:
                num_1 = float(input('First number: '))
                num_2 = float(input('Second number: '))
                return num_1, num_2, sign
            except ValueError:
                print('You must enter a number!')


def calculate():
    while True:
        num_1, num_2, sign = get_operation()
        if sign == '+':
            result = num_1 + num_2
        elif sign == '-':
            result = num_1 - num_2
        elif sign == '*':
            result = num_1 * num_2
        elif sign == '/':
            result = num_1 / num_2
        print(f'Result: {str(result)}\n')


if __name__ == '__main__':
    calculate()
