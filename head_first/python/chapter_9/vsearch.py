def search4vowels(phrase: str) -> set:
    """display any vowels found in supplied word"""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search4letters(phrase: str, letters: str = 'aeiou') -> set:
    """return a set of 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))