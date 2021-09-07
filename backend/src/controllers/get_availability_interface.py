from abc import ABC, abstractmethod


class GetAvailabilityInterface(ABC):

    @abstractmethod
    def get_available_devices(self):
        """get available devices with price information in a mapped form to be exposed on an endpoint"""
        pass

    @abstractmethod
    def get_all_devices(self):
        """get all devices with price information in a mapped form to be exposed on an endpoint"""
        pass
