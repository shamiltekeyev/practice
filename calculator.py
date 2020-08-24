# Calculator


def valid_operation_sign(sign):
    correct_signs = ['+', '-', '*', '/']
    return True if sign in correct_signs else False

def valid_operation_nums(first, second):
    first_is_num, second_is_num = first.isdigit(), second.isdigit()
    return first_is_num and second_is_num


def calculate(first, second, sign):
    is_sign = valid_operation_sign(sign)
    is_nums = valid_operation_nums(first, second)
    if is_sign and is_nums:
        a, b = float(first), float(second)
        if sign == '+':
            result = a + b
        elif sign == '-':
            result = a - b
        elif sign == '*':
            result = a * b
        elif sign == '/':
            result = a / b
        return result
    else:
        print('No sign!')


def main():
    while True:
        print(f'Result: {calculate("1", "2", "+")}')
        break


if __name__ == '__main__':
    main()
