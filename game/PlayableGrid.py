from Grid import Grid
import numpy as np
from GridUtils import merge, getRotatedMatrix, DIRECTIONS

class PlayableGrid(Grid):
  def __init__(self, seed, w=4, h=4):
    super(PlayableGrid, self).__init__(w, h, seed)
    self.moves = 0

  def action(self, direction):
    self.moves += 1
    points, self.arr = self.__get_moved_grid(direction)

    super(PlayableGrid, self)._set_random_tile()

    return points.sum(), self.moves, self.__is_game_over(), self._best_tile()

  def __is_game_over(self):
    for direction in DIRECTIONS:
      arr = self.__get_moved_grid(direction)

      if not np.array_equal(arr, self.arr):
        return False

    return True

  def __get_moved_grid(self, direction):
    arr = getRotatedMatrix(self.arr, self.w, self.h, direction).transpose()

    points = np.zeros((arr.shape[1], 1))

    arr = map(lambda v: 
      np.lib.pad(\
        merge(v[1], points[v[0]]), (self.w, 0), 'constant', constant_values=0 \
      )[-self.w:], enumerate(arr))

    arr = np.array(arr)

    return points, getRotatedMatrix(
      arr.transpose(), self.w, self.h, direction, True\
    ).reshape(self.w * self.h)
