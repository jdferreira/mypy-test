import random

from tqdm.auto import trange

def count(start, stop):
    return sum(trange(start, stop))

if __name__ == '__main__':
    print(count(0, 10_000_000))
