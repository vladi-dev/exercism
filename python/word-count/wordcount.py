# -*- coding: utf-8 -*-
import re
import collections


def word_count(str):
    str = re.sub('[\W\,\_]', ' ', str.decode('utf-8').lower(), flags=re.UNICODE).strip()
    return collections.Counter(str.split())
