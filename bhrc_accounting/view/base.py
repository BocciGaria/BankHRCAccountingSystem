import abc


class IView(abc.ABCMeta):
    """Interface for views

    Describe the interface for views in Tkinter/MVC
    """

    @abc.abstractmethod
    def __init__(self, master):
        """Constructor

        Args:
            master: The master widget for the view
        """
        raise NotImplementedError()
