from patterns.singleton import Singleton                # design pattern (one instance)

class Gui(object, metaclass=Singleton):
    """Class for maintaining measurements about the GUI."""

    # constants
    DEFAULT_WINDOW_WIDTH = 480                  # pixels across
    DEFAULT_WINDOW_HEIGHT = 800                 # pixels up/down        

    def __init__(self):
        """Construct object."""
        self.__width = self.DEFAULT_WINDOW_WIDTH
        self.__height = self.DEFAULT_WINDOW_HEIGHT

    @property
    def width(self):
        """Returns width of GUI window."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the GUI width."""
        # values    width of GUI

        self.__width = value

    @property
    def height(self):
        """Returns height of GUI window."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the GUI height."""
        # values    height of GUI

        self.__height = value
