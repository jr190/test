user_input = int(input('How many Fibonacci numbers would you like to generate? '))


def fib_seq(repeats):
    '''Generates the Fibonacci Sequence'''
    first_num = 1
    second_num = 1
    print(first_num)
    print(second_num)
    third_num = first_num + second_num
    for x in range(repeats):
        first_num = second_num
        second_num = third_num
        third_num = first_num + second_num
        print(third_num)
    return

fib_seq(user_input)
