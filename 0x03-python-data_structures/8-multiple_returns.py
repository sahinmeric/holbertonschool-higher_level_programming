#!/usr/bin/python3
def multiple_returns(sentence):
    if(len(sentence) == 0):
        ret = (0, None)
    else:
        ret = (len(sentence), sentence[0])
    return ret
