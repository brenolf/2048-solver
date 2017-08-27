from Individual import Individual
import numpy as np

class Population(object):
  def __init__(self, input_dim, n_individuals=10):
    self.n_individuals = n_individuals
    self.input_dim = input_dim

    self.generation = 1
    self.individuals = 0

    self.group = []

    for i in xrange(n_individuals):
      self.group.append(Individual(input_dim, self.__get_name()))

  def evolve(self):
    self.generation += 1
    ordered = sorted(self.group, key=lambda i: i.fitness(), reverse=True)

    p20 = int(self.n_individuals * 0.2)

    next_gen = []
    winners = []

    for i in xrange(p20):
      winners.append(ordered[i])

    for i in xrange(p20):
      winners.append(ordered[p20 + i])

    for i in xrange(self.n_individuals - 2 * p20):
      mother = np.random.choice(winners)
      father = np.random.choice(winners)

      child = (mother + father)

      child.name = self.__get_name()

      next_gen.append(child)

    self.group = next_gen + winners

    return ordered[0]

  def __get_name(self):
    self.individuals += 1
    return 'g{}.i{}'.format(self.generation, self.individuals)
