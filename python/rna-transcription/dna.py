import re

map = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
repl = lambda matchobj: map[matchobj.group(0)]

def to_rna(str):
    return re.sub('[AGUCT]', repl, str)