class Step:
    def __init__(self, dx:int, dy:int) -> None:
        """Keeps track of how the x and y coordinates change after taking the step.

        Args:
            dx (int): change in x direction.
            dy (int): change in y direction.
        """

        self.dx = dx
        self.dy = dy

# Initializes the 4 possible steps
steps = {"up": Step(0, 1), "right": Step(1, 0), "down": Step(0, -1), "left": Step(-1, 0)}