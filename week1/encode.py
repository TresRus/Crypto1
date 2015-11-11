#!/usr/bin/python

import sys

def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

def random(size=16):
    return open("/dev/urandom").read(size)

def encrypt(key, msg):
    return strxor(key, msg)

if len(sys.argv) >= 2:
    with open(sys.argv[1]) as f:
        messages = f.readlines()
        key = random(1024)
        for msg in messages:
            m = msg.strip()
            print m
            print m.encode('hex')
            print encrypt(key, m).encode('hex')
