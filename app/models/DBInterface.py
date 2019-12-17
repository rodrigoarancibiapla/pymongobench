from abc import ABC, abstractmethod

class DBInterface(ABC):

    @abstractmethod
    def get_companies(self, number):
        pass
