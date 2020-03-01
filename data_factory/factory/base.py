from abc import ABC, abstractmethod


class FactoryBase(ABC):

    @abstractmethod
    def fetch_data(self):
        pass
