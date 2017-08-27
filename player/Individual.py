import game
from game.GridUtils import DIRECTIONS
from keras.models import Sequential
from keras.layers import Dense, Activation

class Individual(object):
  def __init__(self, input_dim):
    model = Sequential()

    model.add(Dense(units=(input_dim), input_dim=input_dim))
    model.add(Dense(units=4))
    model.add(Activation('softmax'))

    self.model = model
    self.input_dim = input_dim

  def __str__(self):
    for layer in self.model.layers:
      print layer.get_weights()

    return ''

  def get_action(self, input):
    predictions = self.model.predict(input.reshape((-1, self.input_dim)))
    return DIRECTIONS[predictions.argmax()]
