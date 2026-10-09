def get_integer_in_range(prompt, max, min):
    while True:
        try:
            integer = int(input(prompt))
        except ValueError:
            print("invalid input, enter a whole number")
            continue
        if min <= integer <= max:
            return integer
        else:
            print("enter number in range ")


def check_a_list(prompt, list):
    if len(list) == 0:
        print(prompt)
        return False
    else:
        return True
