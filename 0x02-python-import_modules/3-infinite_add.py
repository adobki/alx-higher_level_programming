#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    if len(argv) == 1:
        print(0)
    else:
        total = 0
        for arg_num in argv[1:]:
            total += int(arg_num)
        print('{}'.format(total))
