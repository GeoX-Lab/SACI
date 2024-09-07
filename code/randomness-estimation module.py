import math
from math import log
def unilzcomplexity(array):
    n = len(array)
    unistr = ""
    for i in range(n):
        temp = array[i]
        if temp < 26:
            symn = int(temp) + 65
        else:
            symn = int(temp) + 71
        stra = chr(symn)
        unistr = unistr + stra

    #print(unistr)
    complexity = 1
    prefix_len = 1
    len_substring = 1
    max_len_substring = 1
    pointer = 0
    while prefix_len + len_substring <= len(unistr):
        if(unistr[pointer + len_substring - 1] == unistr[prefix_len + len_substring - 1]):
            len_substring += 1
        else:
            max_len_substring = max(len_substring, max_len_substring)
            pointer += 1
            if pointer == prefix_len:
                complexity += 1
                prefix_len += max_len_substring
                pointer = 0
                max_len_substring = 1
            len_substring = 1
    if len_substring != 1:
        complexity += 1
    return complexity,unistr

def multilzcomplexity(multiarray,a):
    n = len(multiarray)
    multistring = ""
    for i in range(0,n):
        temp = multiarray[i]
        if temp < 26:
            symn = int(temp) + 65
        else:
            symn = int(temp) + 71
        stra = chr(symn)
        multistring = multistring + stra
    complexity = 1
    prefix_len = a
    len_substring = a
    max_len_substring = a
    pointer = 0
    while prefix_len + len_substring <= len(multistring):
        if (multistring[(pointer + len_substring - a):(pointer + len_substring)] == multistring[(prefix_len + len_substring - a):(prefix_len + len_substring)]):
            len_substring += a
        else:
            max_len_substring = max(len_substring, max_len_substring)
            pointer += a
            if pointer == prefix_len:
                complexity += 1
                prefix_len += max_len_substring
                pointer = 0
                max_len_substring = a
            len_substring = a
    if len_substring != a:
        complexity += 1
    return complexity

def norm_unilzcomplexity(array,nse):
    lzcu = unilzcomplexity(array)
    com = lzcu[0]
    unistr = lzcu[1]
    n = len(unistr)
    if n > 1 :
        norm_complexity = com / (n / log(n, nse))
    else:
        norm_complexity = 0
    return norm_complexity

def norm_multilzcomplexity(multistring,nse,a):
    com = multilzcomplexity(multistring,a)
    n = len(multistring)/a
    base = pow(nse, a)
    #print(n,base)
    norm_complexity = com / (n / log(n,base))
    return norm_complexity









