import urllib.parse

string_to_encode = input("Enter string to encode: ")
pass_count = int(input("Encode how many times (default: 1)? ") or 1)


def encode():
    print('** ** ** ** **')
    print("** encoding **")
    print('** ** ** ** **')

    # make the initial encoding pass and reduce passes by 1
    passes = pass_count
    encoded_string = urllib.parse.quote(string_to_encode)
    passes -= 1

    # if there are passes remaining, encode again
    if passes:
        for x in range(passes):
            encoded_string = urllib.parse.quote(encoded_string)

    print('Encoded string: ')
    print(encoded_string)


if __name__ == '__main__':
    encode()


