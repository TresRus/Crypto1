#!/usr/bin/python

import sys, operator

def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

def decode(key, c):
    return strxor(key, c)

def hackAll(key, ciphers):
    newKey = list(hackSpace(key, ciphers))
    shortest = min(ciphers, key=len)
    for chPos in range(0, len(shortest)):
        if newKey[chPos] == chr(0):
            gist = {}
            for cph in ciphers:
                if gist.has_key(cph[chPos]):
                    gist[cph[chPos]] = gist[cph[chPos]] + 1
                else:
                    gist[cph[chPos]] = 1
            newKey[chPos] = strxor(max(gist.iteritems(), key=operator.itemgetter(1))[0], "e")[0]
    return "".join(newKey)

def isAllAlpha(lines, pos):
    for line in lines:
        if not line[pos].isalpha():
            return False
    return True

def hackSpace(key, ciphers):
    newKey = list(key)
    c = " "
    for i in range(0, len(ciphers)):
        xored = []
        d = list(strxor(ciphers[i], c * 1024))
        for j in range(0, len(ciphers)):
            if i != j and len(ciphers[i]) <= len(ciphers[j]):
                xored.append(strxor(ciphers[i], ciphers[j]))
        if len(xored) > 1:
            for chPos in range(0, len(ciphers[i])):
                if isAllAlpha(xored, chPos):
                    newKey[chPos] = d[chPos]

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
        for i in range(0, len(ciphers)):
            cph = ciphers[i]
            print i
            print "Cipher:"
            print cph.encode('hex')
            print "Decode:"
            print decode(key, cph)
