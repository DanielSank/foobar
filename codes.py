"""Level 2"""

def answer(codes):
    """Find number of distinct access codes in a list of possibilities.

    Two codes are equivalent if they are the same or reverses of one
    another. Two codes which are not equivalent are distinct. For
    example, 'abc' is equivalent to 'abc' and 'cba', but not to 'bca'.

    The empty string counts as a code.

    Args:
        codes (list(str)): List of possible access codes. Each code is
            a string containing only letters a-z, all lower case.
            Lenth of this list is never longer than 5000 codes. Each
            code has at most 10 characters.

    Returns (int): number of distinct codes.
    """
    s = set()
    num_distinct_codes = 0
    for code in codes:
        if code in s:
            continue
        elif is_palindrome(code):
            s.add(code)
        else:
            s.add(code)
            s.add(code[::-1])
        num_distinct_codes += 1
    return num_distinct_codes


def is_palindrome(code):
    if code == code[::-1]:
        return True
    else:
        return False
