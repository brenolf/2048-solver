import os

def step(individual, game, score, epoch):
  epoch += 1
  action = individual.get_action(game.arr)
  points, moves, game_over = game.action(action)

  score += points

  print '{} ({}) {} pts'.format(individual.name, epoch, int(score))
  print action
  print game

  individual.set_state(**{
    'score': score,
    'lost': game_over,
    'turns': epoch
  })

  return score, epoch, game_over
