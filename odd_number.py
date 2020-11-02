odd_numbers = []
CRED = '\033[31m'
CGRN = '\033[32m'
CEND = '\033[0m'

def get_value(msg):
    while True:
        try:
            value = int(input(msg))
        except:
            print('{}Input integer digit only!{}'.format(CRED,CEND))
            continue
        else:
            return value
            break



def odd_check(numbers):
    for number in numbers:
        if (number % 2) == 0 and number != 0:
            odd_numbers.append(number)
    return odd_numbers

if __name__ == "__main__":
    first_number = get_value('Input first number:')
    last_number = get_value('Input last number:')
    if first_number == last_number:
        odd_check(range(first_number,first_number+1))
    elif first_number > last_number:
        odd_check(range(last_number,first_number))
    else:
        odd_check(range(first_number, last_number))
    print(
        '{}On the list from {} to {} exists next odd numbers: \n {}{}'.format(CGRN,first_number,last_number,odd_numbers,CEND)
    )
