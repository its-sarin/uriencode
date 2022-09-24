import urllib.parse
import argparse

parser = argparse.ArgumentParser(description='URI encode any given string')
parser.add_argument('input', type=str, help='The string to encode')
parser.add_argument('--pass', '-p', dest='pass_count', type=int, help='Number of times to pass input through the encoding function (default: 1)')
args = parser.parse_args()

string_to_encode = args.input
pass_count = args.pass_count or 1


def encode():
    # make the initial encoding pass and reduce passes by 1
    passes = pass_count
    encoded_string = urllib.parse.quote(string_to_encode)
    passes -= 1

    # if there are passes remaining, encode again
    if passes:
        for x in range(passes):
            encoded_string = urllib.parse.quote(encoded_string)

    print(encoded_string)


if __name__ == '__main__':
    encode()


