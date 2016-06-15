# -*- coding: utf-8 -*-
import re
from collections import Counter


def word_count(str):
    regexp = '\W|_'
    return Counter(word for word in re.split(regexp, str.decode('utf-8').lower(), flags=re.UNICODE) if word != '')
