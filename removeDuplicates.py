# Give it a wordlist of keywords or subdomains and duplicate words will be removed
import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    "list", type=str, help="subs.txt")
args = parser.parse_args()

WORDLIST = args.list


def removeDupes():
    lines = open(WORDLIST, 'r').readlines()

    lines_set = set(lines)

    out = open(WORDLIST, 'w')

    for line in lines_set:
        out.write(line)


if __name__ == '__main__':
    removeDupes()
