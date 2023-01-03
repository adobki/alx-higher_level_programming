#!/usr/bin/python3
def copy_list(some_list):
    return some_list[:] if isinstance(some_list, list) else some_list
