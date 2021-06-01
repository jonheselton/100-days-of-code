import art


def add(number1, number2):
    return number1 + number2


def subtract(number1, number2):
    return number1 - number2


def multiply(number1, number2):
    return number1 * number2


def divide(number1, number2):
    return number1 / number2





def main():
    run_calc = True
    input1 = 0
    while run_calc:
        print(art.logo)
        operation = input('+\n-\n*\n/\n Choose an operation: ')
        if not input1:
            input1 = int(input('first number: '))
        input2 = int(input('second number: '))
        if operation == '+':
            calc = add(input1, input2)
            print(calc)
        elif operation == '-':
            calc = subtract(input1, input2)
            print(calc)
        elif operation == '*':
            calc = multiply(input1, input2)
            print(calc)
        elif operation == '/':
            calc = divide(input1, input2)
            print(calc)
        else:
            print('invalid choice')
        go_again = input('run again with the result? y/n')
        input1 = calc
        if go_again == 'n':
            run_calc = False
    else:
        return


if __name__ == "__main__":
    main()
