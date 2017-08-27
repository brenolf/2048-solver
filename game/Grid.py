import numpy as np

class Grid(object):
  initial_tiles = 2

  def __init__(self, w, h, seed):
    self.w = w
    self.h = h
    self.rand = np.random.RandomState(seed)

  def prepare(self):
    self.arr = np.array([0] * (self.w * self.h))
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

    place = self.rand.choice(spots)
    self.arr[place] = 2 if self.rand.rand() < 0.9 else 4

    return True

  def _best_tile(self):
    return int(self.arr.max())

