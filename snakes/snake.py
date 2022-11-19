import random
from source.step import *

class Snake:
  """Basic snake class which takes random steps at any point."""

  def __init__(self, x:int=0, y:int=0, size:int=3) -> None:
    """Initializes the basic snake class.

    Args:
        x (int, optional): starting x position. Defaults to 0.
        y (int, optional): starting y position. Defaults to 0.
        size (int, optional): size of the body of the snake (including head). Defaults to 3.
    """

    self.x = x
    self.y = y
    self.size = size
    self.body = self.init_body()
    self.tail = self.body[-1]
    self.pathing = False
      
  def step(self, step:Step) -> None:
    """Makes the snake take the input step by updating its coordinates.

    Args:
        step (Step): The step the snake should take
    """

    self.body.insert(0, (self.x, self.y))
    self.x += step.dx
    self.y += step.dy
    self.body.pop()
    self.tail = self.body[-1]

  def next_step(self) -> Step:
    """Determines the next step the snake will take.

    This snake will choose the next step randomly.

    Returns:
        Step: the next step the snake wants to take.
    """

    return steps[random.choice(list(steps))]
  
  def init_body(self) -> list[tuple[int]]:
    """Initializes the body of the snake.

    Creates a list of tuples containing the coordinates of the bodyparts of the snake.

    Returns:
        list[tuple[int]]: list containing the coordinates of the bodyparts
    """
      
    out = []
    for i in range(1, self.size):
      out.append((self.x, self.y-i))

    return out
