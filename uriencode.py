import urllib.parse as urlparse
import argparse

parser = argparse.ArgumentParser(description='uri encode a given string one or more times')
parser.add_argument('-s', '--string', help='The string to be uri-encoded')
parser.add_argument('-c', '--count', default=1, help='Number of times to uri-encode the given string (default: 1)')
parser.add_argument('-a', '--all', action='store_true', help='Force encoding of ALL characters (/ and . included)')
args = parser.parse_args()


def encode():
    # make the initial encoding pass and reduce passes by 1
    passes = int(args.count)

    if args.all:
        encoded_string = urlparse.quote(args.string, safe='')
        encoded_string = encoded_string.replace('.', '%2E')
        encoded_string = encoded_string.replace('~', '%7E')
    else:
        encoded_string = urlparse.quote(args.string)

    passes -= 1

    # if there are passes remaining, encode again
    if passes:
        for x in range(passes):
            encoded_string = urlparse.quote(encoded_string)

    print('Encoded string:')
    print(encoded_string)


if __name__ == '__main__':
    encode()


