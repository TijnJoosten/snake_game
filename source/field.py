class Field:
    def __init__(self, field_type:str) -> None:
        """Keeps track of all possible types each field in the game world can take.

        Args:
            field_type (str): name of the field type.
        """
        
        self.field_type = field_type
    
    def set_field(self, field_type: str) -> None:
        """Changes the current type of the field to the input field type.

        Args:
            field_type (str): new type of the field.
        """

        self.field_type = field_type
    
    def __repr__(self) -> str:
        """Determines how the fields are printed to the console.

        Returns:
            str: representation of the field type. Defaults to 'err' when the current field type is unknown.
        """

        if self.field_type == 'wall':
            return 'x'
        if self.field_type == 'empty':
            return '.'
        if self.field_type == 'head':
            return 'H'
        if self.field_type == 'body':
            return 'B'
        if self.field_type == 'food':
            return 'F'
        return 'err'