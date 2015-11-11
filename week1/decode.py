#!/usr/bin/python

import sys

def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

def decode(key, c):
    return strxor(key, c)

def hackAll(key, ciphers):
    newKey = key
    for i in range(0, len(ciphers)-2):
        for j in range(i+1, len(ciphers)-1):
            for k in range(j+1, len(ciphers)):
                for c in list(" .'"):
                    newKey = hack(newKey, ciphers[i], ciphers[j], ciphers[k], c)
                    newKey = hack(newKey, ciphers[j], ciphers[i], ciphers[k], c)
                    newKey = hack(newKey, ciphers[k], ciphers[j], ciphers[i], c)
    return newKey

def hack(key, c1, c2, c3, ch):
    newKey = list(key)
    x1 = strxor(c1, c2)
    y1 = strxor(x1, ch * 1024)
    x2 = strxor(c1, c3)
    y2 = strxor(x2, ch * 1024)
    d = list(strxor(c1, ch * 1024))
    for i in range(0, min([len(c1), len(c2), len(c3)])):
        if y1[i].isalpha() and y2[i].isalpha():
            newKey[i] = d[i]
    return "".join(newKey)

if len(sys.argv) >= 2:
    with open(sys.argv[1]) as f:
        ciphers = []
        for line in f:
            ciphers.append(line.strip())
        key = chr(0) * 1024
        key = hackAll(key, ciphers)
        print "KEY:"
        print key.encode('hex')
        print len(key)
#        for cph in ciphers:
#            print cph.encode('hex')
#            print decode(key, cph)
