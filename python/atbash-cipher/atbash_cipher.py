from string import lowercase, digits

dec_alpha = list(lowercase)
enc_alpha = sorted(set(lowercase), reverse=True)


def encode(s):
    tmp = []
    s = s.lower()

    # Substitute characters
    for c in s:
        if c in lowercase:
            tmp.append(enc_alpha[dec_alpha.index(c)])
        elif c in digits:
            tmp.append(c)

    # Group characters by 5, separate with space
    i = 0
    res = []
    while i < len(tmp):
        if i > 0 and (i % 5) == 0:
            res.append(' ')
        res.append(tmp[i])
        i += 1

    return ''.join(res)


def decode(s):
    return ''.join([dec_alpha[enc_alpha.index(x)] for x in s.strip().lower() if x in dec_alpha])
