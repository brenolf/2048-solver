import numpy as np
import game
import player
import time
import os

NUMBER_EPOCHS = 70
SLEEP_TIME = 0.01
SEED = 1234

np.random.seed(SEED)

from game.PlayableGrid import PlayableGrid as Game
from player.Population import Population
from player.Individual import Individual
from utils import step

s = SEED

g = Game(SEED)
p = Population(g.w * g.h)
best = None

while True:
  for individual in p.group:
    g.prepare()

    epoch = 0
    score = 0

    while epoch < NUMBER_EPOCHS:
      print 'Best:', best

      score, epoch, game_over = step(individual, g, score, epoch)

      if game_over:
        break

      time.sleep(SLEEP_TIME)
      os.system('clear')

  best = p.evolve()
  print best

  if best.kwstate['best'] == 2048:
    proceed = raw_input('2048! Play with winner?')
    g = Game(s)
    g.prepare()
    score = 0
    epoch = 0

    while epoch < NUMBER_EPOCHS:
      score, epoch, game_over = step(best, g, score, epoch)

      if game_over:
        break

      time.sleep(0.6)
      os.system('clear')


  # proceed = raw_input('proceed?')

  # if proceed == 'N' or proceed == 'n':
  #   break

  s += 1
  g = Game(s)
