import os

def step(individual, game, score, epoch, gen):
  epoch += 1
  action = individual.get_action(game.arr)
  points, moves, game_over, best = game.action(action)

  score += points

  print 'G{}: {} ({}) {} pts - best tile: {}'.format(gen, individual.name, epoch, int(score), best)
  print action
  print game

  individual.set_state(**{
    'score': score,
    'lost': game_over,
    'turns': epoch,
    'best': best
  })

  return score, epoch, game_over
