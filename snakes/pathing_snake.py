from snakes.snake import Snake

class Pathing_Snake(Snake):
    def __init__(self, x:int=0, y:int=0, size:int=3, pathing_iterations:int=5):
        super().__init__(x, y, size)
        self.pathing = True
        self.path = []
        self.path_head = (self.x, self.y)
        self.pathing_iterations = pathing_iterations
        self.pathing_iterations_origin = pathing_iterations
    
    def make_aware(self, world):
        self.world = world

    def next_step(self):
        """Determines the next step the snake will take.

        This snake will choose the next step randomly.

        Returns:
            Step: the next step the snake wants to take.
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
        