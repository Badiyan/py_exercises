CRED = '\033[31m'
CGRN = '\033[32m'
CEND = '\033[0m'


#def printer(msg = str, colors = int, f_value, s_value ): # 1 - green 2 - red 3 - both
#    print()


def checker(first_input,second_input):
    if type(first_input) is int and type(second_input) is int: # int checking
        print(
            'Both values is {c_grn}int{c_end} type'.format(
                c_grn = CGRN,
                c_end = CEND
            )
        )
        if first_input == second_input:
            print(
                'Both numbers is = {c_grn}{value}{c_end}'.format(
                    c_grn = CGRN,
                    c_end = CEND,
                    value = first_input
                )
            )
        elif first_input > second_input:
            print(
                'Bigger is number {c_grn}{value}{c_end}'.format(
                    c_grn = CGRN,
                    c_end = CEND,
                    value = first_input
                )
            )
        else:
            print(
                'Bigger is number {c_grn}{value}{c_end}'.format(
                    c_grn = CGRN,
                    c_end = CEND,
                    value = second_input
                )
            )
    elif type(first_input) is str and type(second_input) is str: # str checking
        print(
            'Both values is {c_grn}str{c_end} type'.format(
                c_grn=CGRN,
                c_end=CEND
            )
        )
        if first_input.find(second_input) >= 0:
            print(
                'String {c_grn}{second_value}{c_end} is substring of {c_grn}{first_value}{c_end}'.format(
                    first_value = first_input,
                    second_value = second_input,
                    c_grn=CGRN,
                    c_end=CEND
                )
            )
        else:
            print(
                'String {c_grn}{second_value}{c_end} is {c_red}not{c_end} substring of {c_grn}{first_value}{c_end}'.format(
                    first_value = first_input,
                    second_value = second_input,
                    c_grn = CGRN,
                    c_red = CRED,
                    c_end = CEND
                )
            )
    else:
        print(
            '{c_red}Error values are unsuitable on this task!{c_end}'.format(
                first_value=first_input,
                second_value=second_input,
                c_red=CRED,
                c_end=CEND
            )
        )

def get_value(input_value):
    in_value = input(input_value)
    try:
        out_value = int(in_value)
    except:
        out_value = in_value
    finally :
        return out_value





if __name__ == "__main__":
    f_number = get_value('Input first value:')
    l_number = get_value('Input last value:')
    checker(f_number, l_number)