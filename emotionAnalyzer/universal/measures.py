from patterns.singleton import Singleton            # design pattern (one instance)
from universal.constants import DEFAULT_WINDOW_WIDTH
from universal.constants import DEFAULT_WINDOW_HEIGHT


class Gui(object, metaclass=Singleton):
    def __init__(self):
        self.__width = DEFAULT_WINDOW_WIDTH
        self.__height = DEFAULT_WINDOW_HEIGHT

    @property
    def width(self):
        """Returns width of GUI window."""
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """Returns height of GUI window."""
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
