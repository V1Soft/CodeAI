import re


def pluralize(word):
    '''This won't be perfect considering how complicated English is. And it's incomplete.'''
    assert type(word) == str, 'Word must be a string'
    if word.endswith('s') or word.endswith('x') or word.endswith('ch') or word.endswith('z'):
        word += 'es'
    else:
        word += 's'
    return(word)
