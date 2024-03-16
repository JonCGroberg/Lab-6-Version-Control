from main import encode, decode

if __name__ == '__main__':
    assert encode(
        "00009962") == "33332295", f'encode("00009962") should return "33332295" but returns {encode("00009962")}'
    assert decode(
        "33332295") == "00009962", f'decode("33332295") should return "00009962" but returns {decode("33332295")}'
