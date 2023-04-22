import abc


class IModel(metaclass=abc.ABCMeta):
    """Interface for models

    Describe the interface for models in Tkinter/MVC
    """

    @abc.abstractmethod
    def get_all(self):
        """Get all records

        Returns:
            The records
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def get_for_primary_key(self, **primary_keys):
        """Get a record for primary key

        Args:
            primary_keys: The primary keys for the record

        Returns:
            The record
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def save(self):
        """Save the record

        Returns:
            None
        """
        raise NotImplementedError()
