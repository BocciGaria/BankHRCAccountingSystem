import abc


class IView(metaclass=abc.ABCMeta):
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

    @abc.abstractmethod
    def create_widgets(self):
        """Create the widgets for the view"""
        raise NotImplementedError()

    @abc.abstractmethod
    def destroy_widgets(self):
        """Destroy the widgets for the view"""
        raise NotImplementedError()

    @abc.abstractmethod
    def grid_widgets(self):
        """Grid the widgets for the view"""
        raise NotImplementedError()

    @abc.abstractmethod
    def forget_widgets(self):
        """Forget the widgets for the view"""
        raise NotImplementedError()

    @abc.abstractmethod
    def remove_widgets(self):
        """Remove the widgets for the view"""
        raise NotImplementedError()


class BaseView(IView):
    """Base class for views

    Base class for views in Tkinter/MVC
    """

    def __init__(self, master):
        self.master = master
        # self.create_widgets()
