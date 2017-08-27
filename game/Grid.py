import random
import numpy as np

class Grid(object):
  initial_tiles = 2

  def __init__(self, w, h):
    self.w = w
    self.h = h
    self.arr = np.array([0] * (w * h))

    random.seed(1234)
    self.__start()

  def __str__(self):
    return '\n'.join(['\t'.join(['{}'] * self.w)] * self.h)\
      .format(*self.arr.astype(int)) + '\n'

  def __find_free_spots(self):
    idx = filter(lambda x: x[1] == 0, enumerate(self.arr))
    return map(lambda x: x[0], idx)

  def __start(self):
    [self._set_random_tile() for _ in xrange(Grid.initial_tiles)]

  def _set_random_tile(self):
    spots = self.__find_free_spots()

    if len(spots) == 0:
      return False

    place = random.choice(spots)
    self.arr[place] = 2 if random.random() < 0.9 else 4

    return True

