
'''remove vovels from string'''

def remove_vovels_from_string(s:str) -> str:

    vovels = 'aeiou'

    for letter in s:
        if letter in vovels:
            s = s.replace(letter, '')

    return s
