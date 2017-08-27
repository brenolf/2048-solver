import numpy as np
import game
import player

np.random.seed(1234)

from game.PlayableGrid import PlayableGrid as Game
from player.Individual import Individual

g = Game()
i = Individual(g.w * g.h)

print i.act(g.arr)
