#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

"""

 Given a number return the next palindrome
 ex. 9 -> 11
     909 -> 919
"""
def next_pal(in1):
    """
    :param in1: input number
    :return: smallest palindrome larger than in1
    """
    import re
    # string of 9's, add 2
    if re.match(r'^9+$', in1):
        return int(in1)+2

    low = in1[:len(in1)/2]

    if len(in1) % 2 != 0:
        mid = in1[len(in1)/2]
    else:
        mid = ""

    if low+mid+low[::-1] > in1:
        return low+mid+low[::-1]

    if mid and mid != '9':
        return low+str(int(mid)+1)+low[::-1]
    elif mid:
        #increment mid
        mid = '0'

    idx = len(low)
    low = list(low)
    while idx:
        if low[idx-1] == '9':
            #increment at current index
            low[idx-1] = '0'
            idx -= 1
        else:
            # next index is not a numeral 9 and
            # can be incremented without carry-over
            low[idx-1] = chr(ord(low[idx-1])+1)
            break

    low = ''.join(low)
    return low+mid+low[::-1]


numtests = int(raw_input(), 10)

for i in range(numtests):
    inp = raw_input().strip()
    if len(inp) > 1000000:
        quit()
    print next_pal(inp)
