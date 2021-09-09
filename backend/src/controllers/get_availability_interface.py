from abc import ABC, abstractmethod
from enum import Enum


class GroupType(Enum):
    ALL = "all"
    AVAILABLE = "available"
    DISABLED = "disabled"
    RESERVED = "reserved"

class GetAvailabilityInterface(ABC):

    @abstractmethod
    def get_device_by_group(self, group_type: GroupType):
        """get devices for defined group with price information in a mapped form to be exposed on an endpoint"""
        pass

    @abstractmethod
    def get_all_devices(self):
        """get all devices with price information in a mapped form to be exposed on an endpoint"""
        pass
