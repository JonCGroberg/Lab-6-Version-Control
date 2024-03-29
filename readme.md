# Lab 6: Password Encoder/Decoder Program

This lab aims to introduce you to version control systems and the concept of version control. You will be working in a
group of two to develop a simplified password encoder/decoder program and practice using version control to manage the
project.

## Specification

Design a simple encoder/decoder program. The program should provide a looping menu that prompts the user to choose
between the encoder and decoder options.
Implement the main function and the encode() function for the program. Push the program to your GitHub repository.
Work in a group of two for this lab. Find your partner's information in "People" -> "Lab 6 Group" and contact them via
Slack or Canvas message.
Add your partner as a collaborator to your GitHub repository.
Clone your partner's encoder program from their GitHub repository and add a decode() function to the solution. Update
your partner's GitHub repository with the final Python file, including both your partner's main and encoder functions,
as well as your decoder function.
Encoder
The password encoder should take an 8-digit password in string format, consisting only of integers. After passing the
password into the encoder, the program should store the encoded password in a new variable. Each digit of the password
should be shifted up by 3 numbers.

## Implementation:

```python
# 8-digit password in string format containing only integers
# Returns new number with each digit being shifted up by 3 numbers
def encode(password: str) -> str:
    res = ""
    for char in password:
        shift: int = (int(char) + 3) % 10  # (9+3) mod 10 = 2
        res += str(shift)
    return res
```

## Testing:

```python
if __name__ == '__main__':
    assert encode(
        "00009962") == "33332295", f'encode("00009962") should return "33332295" but returns {encode("00009962")}'
    assert decode(
        "33332295") == "00009962", f'decode("33332295") should return "00009962" but returns {decode("33332295")}'

```

## Examples:

`"12345555"` becomes `"45678888"` after encoding.
`"00009962"` becomes `"33332295"`after encoding.

## Decoder

The password decoder takes an encoded password and returns the original password. For example, "45678888" needs to be
decoded back to "12345555".