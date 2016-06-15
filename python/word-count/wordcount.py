# -*- coding: utf-8 -*-
import re


def word_count(str):
    r = dict()
    str = str.decode('utf-8')
    str = re.sub('[\W\,\_]', ' ', str.lower(), flags=re.UNICODE).strip()
    for w in str.split():
        r[w] = r[w] + 1 if w in r else 1
    return r
