class Singleton(type):
    """Singleton pattern metaclass."""

    # variables
    __instance = None         # single object instance

    def __init__(cls, name, bases, dic):
        """Constructs object."""
        # name  string containing the name of the class
        # bases tuple of classes from which the current class derives
        # dic   dictionary of all methods and fields defined in the class

        # call constructor on all parents
        super(Singleton, cls).__init__(name, bases, dic)

    def __call__(cls, *args, **kw):
        """Returns oject instance and create new if needed."""
        # *args non-keyworded variable length argument
        # **kw  keyworded variable length argument

        if cls.instance is None:                    # instance already created?
            # create new instance
            cls.__instance = super(Singleton, cls).__call__(*args, **kw)
        return cls.__instance                       # return the instance

    @property
    def instance(cls):
        """Returns object instance"""
        return cls.__instance
