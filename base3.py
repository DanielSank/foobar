"""level 2"""

from __future__ import division


def answer(n):
    """Balance a scale with weight n on left side, using objects of mass 3**i.

    Algorithm:

    Consider a weight n which, expressed in base 3 has the following
    coefficients for each power:

    coefficient    [0, 1, 1, 2, 1]
    power           0  1  2  3  4

    We balance against this by iterively checking where to put each of our one
    objects of mass 3**i.

    In the place for power=0 we find a 0 which means the
    weight n has no component of mass 3**0 = 1. Therefore, we don't need our
    0th object.

    In the place for power=1 we find a 1 meaning that we can balance this part
    of n's mass with our single object of mass 3**1. Therefore, we put the
    object on the right of the scale. We do the same for the place for power=2
    where we also find a 1.

    In the place for power=3 we find a 2. We cannot balance this by putting an
    object on the right, so instead we imagine putting it on the left. This
    effectively bumps the coefficient from 2 to 3, which carries to the next
    place and effectively leaves a 0 behind. Therefore, we place the object on
    the left, and then modify the coefficients list by adding +1 to the next
    element.

    If we find a coefficient 3 that means we used to be a 2 but picked up a
    carry. This should really be a 0 with the carry passed on to the next place.

    Args:
        n (int): The mass we wish to balance.

    Returns (str):
        The ith character in the string represents on which side of the scale we
            should place the ith mass (which has value 3**i). A character 'L'
            means to place the number along with the one we're trying to
            balance. A character 'R' means to place it on the other side. A
            character '-' means to not use that mass.
    """
    coefficients = base_powers(n, 3)
    what_to_do_with_powers = []

    for power in range(len(coefficients)):
        coefficient = coefficients[power]
        if coefficient == 0:
            what_to_do_with_powers.append('-')
        elif coefficient == 1:
            what_to_do_with_powers.append('R')
        elif coefficient == 2:
            what_to_do_with_powers.append('L')
        elif coefficient == 3:  # Carry from previous step
            what_to_do_with_powers.append('-')
        if coefficient == 2 or coefficient == 3:
            try:
                coefficients[power + 1] += 1
            except IndexError:
                what_to_do_with_powers.append('R')
    # The un-pythonic iteration style here avoids mutating a list while
    # iterating over it.

    return what_to_do_with_powers


def base_powers(n, base):
    """Represent an integer to a certain base.

    Args:
        n (int): Integer we wish to decompose into a base.
        base (int): Number base to use for representation.

    Returns (list(int)): The ith element in the list is the coefficient of
        base**i for n. These elements are always in the range {0, 1,...base-1}.
        For example, if we're trying to represent the number 5 in base 3 we
        would return [2, 1] meaning 5 = 1*3**0 + 2*3**1.
    """

    highest_power = 0
    while 1:
        if 2 * base**highest_power >= n:
            break
        else:
            highest_power += 1

    coefficients = []
    remaining = n
    power = highest_power

    while power >= 0:
        coefficient = remaining // base**power
        coefficients.append(coefficient)
        remaining -= coefficient * base**power
        power -= 1
    return coefficients[::-1]
