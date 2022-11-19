import random
from source.field import Field

class World:
    """Keeps track of the state of the game. This includes the world and the run loop."""

    def __init__(self, snake, size:int, max_iter:int=10, only_legal_moves:bool=False) -> None:
        """Initializes the world. This contains adding the snake and generating the first food.

        Args:
            snake: snake to be added to the world.
            size (int): size of the world, in both the x and y direction.
            max_iter (int, optional): max number of iterations of the game loop. Defaults to 10.
            only_legal_moves (bool, optional): Determines if the snake is only allowed to take legal moves. If false, the game will end otherwise. Defaults to False.
        """

        self.snake = snake
        self.size = size
        self.only_legal_moves = only_legal_moves
        self.max_iter = max_iter

        self.world = self.init_world()
        self.add_snake()
        self.generate_food()
        self.alive = True
        self.iter = 0

  
    def init_world(self) -> list[Field]:
        """Initializes the world by creating empty fields surrounded by walls.

        Returns:
            list[Field]: list containing the initialized fields.
        """

        out = []
        for i in range(self.size+2):
            for j in range(self.size+2):
                if i == 0 or i == self.size+1 or j ==0 or j == self.size+1:
                    out.append(Field('wall'))
                else:
                    out.append(Field('empty'))
        return out

    def run(self) -> None:
        """Runs the game while the snake is alive or while the max number of iterations has not been reached.

        At each step, the snake determines what step to take. It will take it if this step is possible, otherwise it will do nothing 
        or the game will end depending on only_legal_moves. If the snake eats food, a new bodypart is added and a new food is generated.
        At each step, the current state of the world is printed.
        """

        while(self.alive):
            self.iter += 1
            if self.snake.pathing:
                (step, (x, y)) = self.snake.next_step()
                self.set_field(x, y, step)
            else:
                next_step = self.snake.next_step()
                next_x = self.snake.x + next_step.dx
                next_y = self.snake.y + next_step.dy
                if self.get_field(next_x, next_y) == 'wall' or self.get_field(next_x, next_y) == 'body':
                    if not self.only_legal_moves:
                        self.alive = False
                else:
                    if self.get_field(next_x, next_y) == 'food':
                        self.snake.body.append(self.snake.tail)
                        self.generate_food()
                    else:
                        self.set_field(self.snake.tail[0], self.snake.tail[1], 'empty')
                        self.set_field(self.snake.x, self.snake.y, 'body')
                        self.snake.step(next_step)
                        self.set_field(self.snake.x, self.snake.y, 'head')

            print(self)
            if self.iter > self.max_iter:
                self.alive = False
    
    def get_field(self, x:int, y:int) -> str:
        """Returns the type of the field.

        Args:
            x (int): x-coordinate of the requested field.
            y (int): y-coordinate of the requested field.

        Returns:
            str: type of the requested field.
        """

        return self.world[x+1 + (y+1) * (self.size+2)].field_type
  
    def set_field(self, x:int, y:int, field_type:Field) -> None:
        """Changes the type of a field.

        Args:
            x (int): x-coordinate of the requested field.
            y (int): y-coordinate of the requested field.
            field_type (Field): the new type of the field.
        """

        self.world[x+1 + (y+1) * (self.size+2)].set_field(field_type)

    def generate_food(self) -> None:
        """Generates new food at a random empty space in the world."""

        random.choice([field for field in self.world if field.field_type == 'empty']).set_field('food')
  
    def add_snake(self) -> None:
        """Adds the snake to the world by changing the types of the corresponding fields."""

        self.set_field(self.snake.x, self.snake.y, 'head')
        for (x, y) in self.snake.body:
            self.set_field(x, y, 'body')

    def __repr__(self) -> str:
        """Creates a representation of the world by converting each field to a character.

        Returns:
            str: string depicted the current state of the world.
        """
        
        out = ''
        for y in range(self.size+2):
            for x in range(self.size+2):
                out += str(self.world[x + y * (self.size+2)])
            out += '\n'

        return out