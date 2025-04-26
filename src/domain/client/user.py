from abc import ABC, abstractmethod


class User(ABC):
    @abstractmethod
    def make_trip(self):
        pass

    @abstractmethod
    def cancel_trip(self):
        pass
