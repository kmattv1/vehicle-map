from abc import ABC

from src.controllers.get_availability_interface import GetAvailabilityInterface, GroupType
from src.entities.response_dto import VehiclesCategorizedByAvailability
from src.repositories.vehicle_info_interface import VehicleInfoInterface, VehicleInfoData
from src.use_cases.vehicle_info_mapper_interface import VehicleInfoMapperInterface


class GetAvailability(GetAvailabilityInterface, ABC):

    def __init__(self,
                 vehicle_information_resource: VehicleInfoInterface,
                 vehicle_information_mapper: VehicleInfoMapperInterface):
        self.vehicle_information_resource = vehicle_information_resource
        self.vehicle_information_mapper = vehicle_information_mapper

    async def get_device_by_group(self, group_type: GroupType) -> VehiclesCategorizedByAvailability:
        price_and_availability_data: VehicleInfoData = await self.vehicle_information_resource.get_price_and_availability_data()
        response: VehiclesCategorizedByAvailability = self.vehicle_information_mapper.group_and_map_data(
            price_and_availability_data.bikes.data['bikes'],
            price_and_availability_data.plans.data['plans']
        ).unwrap()

        if group_type == GroupType.ALL:
            return response
        if group_type == GroupType.AVAILABLE:
            return VehiclesCategorizedByAvailability(available=response.available, reserved=[], disabled=[])
        if group_type == GroupType.DISABLED:
            return VehiclesCategorizedByAvailability(available=[], reserved=[], disabled=response.disabled)
        if group_type == GroupType.RESERVED:
            return VehiclesCategorizedByAvailability(available=[], reserved=response.reserved, disabled=[])

    async def get_all_devices(self) -> VehiclesCategorizedByAvailability:
        price_and_availability_data: VehicleInfoData = await self.vehicle_information_resource.get_price_and_availability_data()
        response = self.vehicle_information_mapper.group_and_map_data(
            price_and_availability_data.bikes.data['bikes'],
            price_and_availability_data.plans.data['plans']
        ).unwrap()
        return response
