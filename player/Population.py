from Individual import Individual

class Population(object):
  def __init__(self, n_individuals=10):
    self.n_individuals = n_individuals
    self.group = [Individual()] * n_individuals


    
