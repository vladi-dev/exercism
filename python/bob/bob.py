import string
def hey(what):
    what = what.strip()

    # I don't understand
    if not len(what):
        return 'Fine. Be that way!'
    # Don't shout at me
    elif what.isupper():
        return 'Whoa, chill out!'
    # Ask my anything
    elif what.endswith('?'):
        return 'Sure.'
    # Nice talking to you
    else:
        return 'Whatever.'
