# -*- coding: utf-8 -*-
import re
import collections


def word_count(str):
    r = dict()
    str = str.decode('utf-8')
    str = re.sub('[\W\,\_]', ' ', str.lower(), flags=re.UNICODE).strip()
    return collections.Counter(str.split())
