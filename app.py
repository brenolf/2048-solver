import numpy as np
import game
import player
import time
import os

NUMBER_EPOCHS = 30
SLEEP_TIME = 0.01
SEED = 1234

np.random.seed(SEED)

from game.PlayableGrid import PlayableGrid as Game
from player.Population import Population
from player.Individual import Individual
from utils import step

g = Game(SEED)
p = Population(g.w * g.h, 6)

for individual in p.group:
  g.prepare()

  epoch = 0
  score = 0

  while epoch < NUMBER_EPOCHS:
    score, epoch, game_over = step(individual, g, score, epoch)

    if game_over:
      break

    time.sleep(SLEEP_TIME)
    os.system('clear')

p.evolve()
