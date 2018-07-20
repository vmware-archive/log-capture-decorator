from __future__ import print_function

import sys


def main():
    stream = sys.argv[1]
    print("Capturing logs on {}".format(stream))

    while True:
        line = sys.stdin.readline()
        # on push, sys.stdin reads tons of blank lines
        if line.strip() != "":
            if stream == 'stderr':
                print('[log-capture on {}]'.format(stream), line, file=sys.stderr)
            else:
                print('[log-capture on {}]'.format(stream), line, file=sys.stdout)


if __name__ == "__main__":
    main()
