
def EvenOrOdd():
    user_input = input('Enter a number: ')

    if int(user_input) % 2 == 0:
        if int(user_input) % 4 == 0:
            print('Definitely not a virus...')
            return
        print('Even')
    else:
        print('Odd')
    return
EvenOrOdd()

def NumCheck():
    user_input = input('Please enter a number: ')
    user_input_two = input('Please enter a second number: ')
    if int(user_input) % int(user_input_two) == 0:
        print('Divides evenly!')
    else:
        print('Does not divide evenly!')
    return
NumCheck()
