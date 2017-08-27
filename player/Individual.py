import numpy as np
import game
from game.GridUtils import DIRECTIONS
from keras.models import Sequential
from keras.layers import Dense, Activation

class Individual(object):
  def __init__(self, input_dim):
    model = Sequential()

    model.add(Dense(units=(input_dim), input_dim=input_dim, bias_initializer='ones'))
    model.add(Dense(units=4, bias_initializer='ones'))
    model.add(Activation('softmax'))

    self.model = model
    self.input_dim = input_dim

  def __str__(self):
    for layer in self.model.layers:
      print '>', layer.get_weights()

    return '--'

  def get_action(self, input):
    predictions = self.model.predict(input.reshape((-1, self.input_dim)))
    return DIRECTIONS[predictions.argmax()]

  def set_state(self, *state, **kwstate):
    self.state = state
    self.kwstate = kwstate

  def mutate(self):
    for layer in self.model.layers:
      w = layer.get_weights()

      if len(w) == 0:
        continue

      inputs, bias = w

      for i in xrange(len(inputs)):
        m = np.random.random(inputs[i].shape[0])
        n = np.random.random(inputs[i].shape[0])
        inputs[i] += m * 2 + n

      layer.set_weights(np.array([inputs, bias]))

    return self


  def __add__(self, individual):
    child = Individual(self.input_dim)

    sets = zip(self.model.layers, individual.model.layers, child.model.layers)

    for (mother, father, offspring) in sets:
      mother_w = mother.get_weights()
      father_w = father.get_weights()

      if len(mother_w) == 0:
        continue

      inputs_mother, bias_mother = mother_w
      inputs_father, bias_father = father_w

      inputs = []
      bias = []

      for i in xrange(len(inputs_mother)):
        coin = np.random.random()
        neuron = inputs_mother if coin <= 0.5 else inputs_father
        inputs.append(np.copy(neuron[i]).tolist())

      for i in xrange(len(bias_mother)):
        coin = np.random.random()
        neuron = bias_mother if coin <= 0.5 else bias_father
        bias.append(np.copy(neuron[i]).tolist())

      inputs = np.array(inputs)
      bias = np.array(bias)

      offspring.set_weights(np.array([inputs, bias]))

    return child
