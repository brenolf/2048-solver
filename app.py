import game
from game.PlayableGrid import PlayableGrid as Game

g = Game()

print g

g.action('right')
g.action('right')
g.action('left')
g.action('left')

print g

g.action('down')

print g

g.action('down')

print g
