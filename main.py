from source.world import *
from snakes.pathing_snake import *

snake = Pathing_Snake(2, 2)

world5= World(snake, 5, only_legal_moves=True, max_iter=20)
snake.make_aware(world5)
print(world5)
world5.run()