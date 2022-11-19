class Step:
    def __init__(self, dx:int, dy:int, name:str) -> None:
        """Keeps track of how the x and y coordinates change after taking the step.

        Args:
            dx (int): change in x direction.
            dy (int): change in y direction.
            name (str): name of direction.
        """

        self.dx = dx
        self.dy = dy
        self.name = name

# Initializes the 4 possible steps
steps = {"down": Step(0, 1, "down"), "right": Step(1, 0, "right"), "up": Step(0, -1, "up"), "left": Step(-1, 0, "left")}