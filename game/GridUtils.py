import numpy as np

DIRECTIONS = ['down', 'left', 'up', 'right']

def getRotatedMatrix(arr, w, h, direction, undo=False):
  i = -1 if undo else 1
  dir = i * DIRECTIONS.index(direction)

  return np.rot90(arr.reshape(w, h), dir)

def merge(vector, points):
  vector = filter(lambda x: x > 0, vector)
  vector, points_got = __merge(vector)

  while True:
    new_vector, aux = __merge(vector)

    if np.array_equal(new_vector, vector):
      break
    
    vector = new_vector
    points_got += aux

  points[0] = points_got

  return vector

def __merge(vector):
  if len(vector) <= 1:
    return vector, 0

  sub, points = __merge(vector[1:])

  if vector[0] == sub[0]:
    sub[0] = sub[0] * 2
    return sub, points + sub[0]

  return [vector[0]] + sub, points
