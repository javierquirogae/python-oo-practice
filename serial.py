"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        '''create instance with start value'''
        self.start = start
        self.gen = start - 1
    
    def __repr__(self):
        """Show representation."""

        return f"<SerialGenerator start={self.start} next={self.gen + 1}>"

        
    def generate(self):
        """Return next serial."""
        self.gen += 1
        return self.gen

    def reset(self):
        """Reset number to original start."""
        self.gen = self.start - 1

