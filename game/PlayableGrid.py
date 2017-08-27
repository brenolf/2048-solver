from Grid import Grid
import numpy as np
from GridUtils import merge, getRotatedMatrix

class PlayableGrid(Grid):
  def __init__(self, w=4, h=4):
    super(PlayableGrid, self).__init__(w, h)
    self.moves = 0

  def action(self, direction):
    self.moves += 1

    arr = getRotatedMatrix(self.arr, self.w, self.h, direction).transpose()

    points = np.zeros((arr.shape[1], 1))

    arr = map(lambda v: 
      np.lib.pad(\
        merge(v[1], points[v[0]]), (self.w, 0), 'constant', constant_values=0 \
      )[-self.w:], enumerate(arr))

    arr = np.array(arr)

    self.arr = getRotatedMatrix(
      arr.transpose(), self.w, self.h, direction, True\
    ).reshape(self.w * self.h)

    super(PlayableGrid, self)._set_random_tile()

    return points.sum(), self.moves
