import re
from string import lower, lowercase

def is_pangram(str):
    return False if not len(str) else not(re.sub('[{}]'.format(lower(str)), '', lowercase))


