import abc

from bhrc_accounting.view.widget import base_widget as bw


class IController(metaclass=abc.ABCMeta):
    """Interface for controllers

    Describe the interface for controllers in Tkinter/MVC
    """

    @abc.abstractmethod
    def __init__(self, master: bw.ITclComposite):
        """Constructor

        Args:
            master: The master widget for the view
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def run(self):
        """Run the controller

        Returns:
            None
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def stop(self):
        """Stop the controller

        Returns:
            None
        """
        raise NotImplementedError()


class BaseController(IController):
    """Base class for controllers

    Base class for controllers in Tkinter/MVC
    """

    def __init__(self, master: bw.ITclComposite):
        self.master = master
