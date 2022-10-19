from source.world import *
from snakes.snake import *

snake = Snake(2, 2)

world5= World(snake, 5, only_legal_moves=True, max_iter=10)
print(world5)
world5.run()