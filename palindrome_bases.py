"""Level 1 (on @google account)"""


from __future__ import division


def answer(n):
    """Find lowest base (>=2) for which integer's representation is palindrome.

    Args:
        n (int): The integer in question.

    Returns (int): Lowest number base in which the representation of n is a
        palindrome.

    Examples:
        answer(42)
            4

        answer(0)
            2
    """
    base = 2
    while 1:
        if is_palindrome(rep_in_base(n, base)):
            break
        else:
            base += 1
    return base


def rep_in_base(n, b):
    """Get list of digits representating an integer in a number base.

    Args:
        n (int): Number to represent.
        b (int): Base

    Returns a string represenation of n in base b. For example, if we choose
        n = 100 and b = 2 then the string would be '1100100'.

    We could optimize the discovery of the largest power and computation of the
    digits if we were to use the fact that we know n<1000, but instead I choose
    to write the function so that it will work on any n
    """
    dominating_power = 0
    while 1:
        if b**dominating_power >= n:
            break
        else:
            dominating_power += 1

    if b**dominating_power > n:
        largest_power = dominating_power - 1

    remainder = n
    s = []
    for power in range(largest_power + 1)[::-1]:
        digit = remainder // b**power
        s.append(digit)
        remainder -= digit * (b**power)
    return s


def is_palindrome(s):
    """Check if a list is a palindrome"""
    return s == s[::-1]
