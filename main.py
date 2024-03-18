# Jonathan Groberg
# UFID :11973817

def decode(password: str) -> str:
    result = ""
    for digit in password:
        new_digit = (int(digit) - 3) % 10
        result += str(new_digit)
    return result


# Jonathan Groberg
# 8-digit password in string format containing only integers
# Returns new number with each digit being shifted up by 3 numbers
def encode(password: str) -> str:
    res = ""
    for char in password:
        shift: int = (int(char) + 3) % 10  # (9+3) mod 10 = 2
        res += str(shift)
    return res


def show_menu() -> None:
    decoded, encoded = None, None  # init it 0,

    while True:
        # menu
        print("Menu")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        option: str = input("Please enter an option: ")
        password: str = "<PASSWORD>"

        if option == "1":  # get password and encode it
            password = input("Please enter your password to encode: ")
            encoded = encode(password)
            print("Your password has been encoded and stored!")

        elif option == "2":
            if encoded is not None:  # user must encode first
                decoded = decode(encoded)  # decode the encoded password
                print(f'The encoded password is {encoded}, and the original password is {decoded}')
            else:  # if there is no encoded password then reprompt user
                continue
        else:
            quit()


if __name__ == '__main__':
    show_menu()
