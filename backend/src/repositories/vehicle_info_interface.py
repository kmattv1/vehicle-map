from abc import ABC, abstractmethod


class VehicleInfoInterface(ABC):

    @abstractmethod
    def get_availability_data(self):
        """get vehicle availability information from downstream"""
        pass

    @abstractmethod
    def get_price_data(self):
        """get vehicle price information from downstream"""
        pass
