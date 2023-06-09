#
# This script calculates entropy
# of specified file.
#
import argparse
import os
import pathlib
import math

chars = [0] * 256

def calculate_entropy(bytes, size):
    entropy = 0
    for b in bytes:
        if b == 0:
            continue
        fi = b / size
        entropy -= fi * math.log2(fi)
    print(entropy)

def main():
    size = 0
    with open(args.file, 'rb') as file:
        while True:
            b = file.read(1)
            if not b:
                break
            chars[int.from_bytes(b, 'big')] += 1
            size += 1
    calculate_entropy(chars, size)
    

if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Script calculates entropy of file',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-f', '--file', help='File whose entropy is to be calculated',
                        required=True,
                        type=pathlib.Path,
                        metavar='FILE')
    args = parser.parse_args()
    main()

