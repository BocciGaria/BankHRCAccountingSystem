import abc


class ISqlClause(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self) -> None:
        raise NotImplementedError()


class ISqlBuilder(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self) -> None:
        raise NotImplementedError()
