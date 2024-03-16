from main import encode, decode

if __name__ == '__main__':
    assert encode("00009962") == "33332295"
    assert decode("33332295") == "00009962"
