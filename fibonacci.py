# The Fibonacci sequence.


def up_to_index(index):
    "This function return the Fibonacci sequence up to N-element."
    if index >= 0:
        fib_sequence = [0, 1]
        if index == 1:
            return fib_sequence[0]
        elif index == 2:
            return fib_sequence
        else:
            for i in range(index - 2):
                fib_sequence.append(fib_sequence[-2] + fib_sequence[-1])
            return fib_sequence
    else:
        return 'You must enter a natural number!'


if __name__ == '__main__':
    try:
        print(up_to_index(int(input('N: '))))
    except ValueError:
        print('You must enter a natural number!')
