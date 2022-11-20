from snakes.snake import Snake

class Pathing_Snake(Snake):
    """Basic pathing snake class which first creates a path using random steps before taking the steps."""

    def __init__(self, x:int=0, y:int=0, size:int=3, pathing_iterations:int=5):
        """Initialises the basic pathing snake class.

        Args:
            x (int): Starting x-coordinate of the head of the snake. Defaults to 0.
            y (int): Starting y-coordinate of the head of the snake. Defaults to 0.
            size (int): The total sizez of the snake including the head. Defaults to 3.
            pathing_iterations (int): Number of iterations the snake will compute the path. 
                                      If max has been reached, the snake will follow this path. Defaults to 5.
        """

        super().__init__(x, y, size)
        self.pathing = True
        self.path = []
        self.path_head = (self.x, self.y)
        self.pathing_iterations = pathing_iterations
        self.pathing_iterations_origin = pathing_iterations
    
    def make_aware(self, world):
        """Gives the snake full access to the game world.

        Used to give the snake knowledge about the world such that it can make better decisions.

        Args:
            world (World): The game world in which the snake lives.
        """

        self.world = world

    def next_step(self):
        """Determines the next step the snake will take.

        First, the snake will create a path containing the steps. 
        Afterwards it will follow this path by taking the consecutive steps.

        Returns:
            Step: the next step the snake it is going to take or the step it wants to take at a given coordinate.
        """
        
        if self.pathing:
            next_head = self.body[0]
            while self.world.get_field(*next_head) != 'empty':
                print(self.world.get_field(*next_head))
                next_step = super().next_step()
                next_head = (self.path_head[0]+next_step.dx, self.path_head[1]+next_step.dy)
            print(self.world.get_field(*next_head))
            self.path.append(next_step)
            old_path_head = self.path_head

            self.path_head = next_head
            self.pathing_iterations -= 1
            if self.world.get_field(*self.path_head) == 'food':
                self.pathing = False
            if self.pathing_iterations == 0:
                self.pathing = False
            return (next_step.name, old_path_head)
        
        next_step = self.path.pop(0)
        if len(self.path) == 0:
            self.pathing = True
            self.pathing_iterations = self.pathing_iterations_origin
        return next_step
        