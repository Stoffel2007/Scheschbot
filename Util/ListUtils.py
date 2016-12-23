from collections import Sequence
from itertools import chain, count


def maxdepth(seq):  # http://stackoverflow.com/a/6040217 Do not use this method with strings!
    seq = iter(seq)
    try:
        for level in count():
            seq = chain([next(seq)], seq)
            seq = chain.from_iterable(s for s in seq if isinstance(s, Sequence))
    except StopIteration:
        return level


if __name__ == '__main__':
    liasdst = [[], [[]], [[[]]]]
    print(maxdepth(liasdst))
