import numpy as np
import game
import player
import time
import os

np.random.seed(1234)

from game.PlayableGrid import PlayableGrid as Game
from player.Individual import Individual

g = Game()
i = Individual(g.w * g.h)

epoch = 0
score = 0

print g
time.sleep(0.5)

while epoch < 100:
  epoch += 1

  action = i.get_action(g.arr)
  points, moves, game_over = g.action(action)

  score += points

  os.system('clear')

  print '{}) {} pts'.format(epoch, int(score))
  print action
  print g

  if game_over:
    break

  i.set_state(**{
    'score': score,
    'lost': game_over,
    'turns': epoch
  })

  time.sleep(0.5)
