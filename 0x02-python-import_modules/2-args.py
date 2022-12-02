#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    argc = len(argv) - 1
    arg_text = " arguments"
    if argc == 0:
        print('{}{}.'.format(argc, arg_text))
    elif argc == 1:
        print('{}{}:'.format(argc, arg_text[:-1]))
        print('{}: {}'.format(argc, argv[1]))
    else:
        print('{}{}:'.format(argc, arg_text))
        argc = 0
        for arg in argv:
            if argc != 0:
                print('{}: {}'.format(argc, arg))
            argc += 1
