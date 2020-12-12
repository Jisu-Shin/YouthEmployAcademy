# -*- coding: utf-8 -*-

def add(*args):
    return sum(args)

def multi(*args):
    result = 1
    for i in args:
        result = result * i
    return result

def whynot(*args):
    print("왜안돼")
    