import re
from string import lower

def word_count(str):

    r = dict()
    str = re.sub('\W', ' ', lower(str))
    str = re.sub('\s{2,}', ' ', str).strip()
    for w in str.split(' '):
        r[w] = r[w] + 1 if w in r else 1

    return r
