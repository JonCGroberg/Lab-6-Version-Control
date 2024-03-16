def show_menu():
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


def decode(password: str) -> str:
    pass


def encode(password: str) -> str:
    pass


if __name__ == '__main__':
    show_menu()
