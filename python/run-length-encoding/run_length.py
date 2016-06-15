# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re

def encode(line):
    i = 0
    count = 1
    prev = ''
    result = ''

    while i <= len(line):
        char = line[i] if i < len(line) else ''

        if char == prev:
            count += 1
        else:
            result += str(count) + prev if count > 1 else prev
            count = 1

        prev = char
        i += 1

    return result


def decode(line):
    regexp ='\d+\w{1}|\d+\s{1}|\w{1}|\s{1,}'
    matches = re.findall(regexp, line, flags=re.IGNORECASE|re.UNICODE)

    decoded = []
    for match in matches:
        count = int(filter(str.isdigit, str(match)) or 1)
        decoded.append(count * match.lstrip(str(count)))

    return ''.join(decoded)
