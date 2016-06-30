def abbreviate(s):
    res = []
    prev = ''
    for c in s:
        if (c.isupper() and not prev.isupper()) or (prev == ' ' or prev == '-'):
            res.append(c.upper())
        prev = c

    return ''.join(res)
