from functools import partial
from typing import List

from returns._internal.pipeline.flow import flow
from returns.pointfree import bind
from returns.result import safe, Result

from src.entities.free_bike_dto import Bike
from src.entities.pricing_plans_dto import Plan
from src.entities.response_dto import VehiclesCategorizedByAvailability, Vehicle
from src.use_cases.vehicle_info_mapper_interface import VehicleInfoMapperInterface, BikeWithPrice, FilteredBikesWithPrice


class VehicleInfoMapper(VehicleInfoMapperInterface):

    @staticmethod
    def price_list_to_dict(pricing_data: List[Plan]):
        price_dict = {}
        for pricing in pricing_data:
            price_dict[pricing['plan_id']] = pricing['description']
        return price_dict

    @staticmethod
    def bike_with_price_to_vehicle(bike_with_price: BikeWithPrice) -> Vehicle:
        return Vehicle(id=bike_with_price.bike_id,
                       lat=bike_with_price.lat,
                       lon=bike_with_price.lon,
                       vehicle_type_id=bike_with_price.vehicle_type_id,
                       pricing_description=bike_with_price.pricing_description)

    @staticmethod
    def add_price_for_bike(bike: Bike, price_dict) -> BikeWithPrice:
        return BikeWithPrice(bike_id=bike['bike_id'],
                             lat=bike['lat'],
                             lon=bike['lon'],
                             is_reserved=bike['is_reserved'],
                             is_disabled=bike['is_disabled'],
                             vehicle_type_id=bike['vehicle_type_id'],
                             current_range_meters=bike['current_range_meters'],
                             pricing_plan_id=bike['pricing_plan_id'],
                             rental_uris=bike['rental_uris'],
                             pricing_description=price_dict[bike['pricing_plan_id']]
                             )

    @staticmethod
    @safe
    def merge_price_and_vehicle_data(vehicle_data: List[Bike],
                                     pricing_data: List[Plan]) -> List[BikeWithPrice]:
        price_dict = VehicleInfoMapper.price_list_to_dict(pricing_data)
        res = list(map(partial(VehicleInfoMapper.add_price_for_bike, price_dict=price_dict), vehicle_data))
        return res

    @staticmethod
    @safe
    def filter_response(vehicles: List[BikeWithPrice]) -> FilteredBikesWithPrice:
        available: List[BikeWithPrice] = []
        reserved: List[BikeWithPrice] = []
        disabled: List[BikeWithPrice] = []

        for vehicle in vehicles:
            if not vehicle.is_disabled and not vehicle.is_reserved:
                available.append(vehicle)

            if not vehicle.is_disabled and vehicle.is_reserved:
                reserved.append(vehicle)

            if vehicle.is_disabled:
                disabled.append(vehicle)

        return FilteredBikesWithPrice(available, reserved, disabled)

    @staticmethod
    @safe
    def map_response(filtered_bikes: FilteredBikesWithPrice) -> VehiclesCategorizedByAvailability:
        return VehiclesCategorizedByAvailability(
            available=list(map(VehicleInfoMapper.bike_with_price_to_vehicle, filtered_bikes.available)),
            reserved=list(map(VehicleInfoMapper.bike_with_price_to_vehicle, filtered_bikes.reserved)),
            disabled=list(map(VehicleInfoMapper.bike_with_price_to_vehicle, filtered_bikes.disabled))
        )

    @staticmethod
    def group_and_map_data(vehicle_data: List[Bike],
                           pricing_data: List[Plan]) -> Result[VehiclesCategorizedByAvailability, Exception]:
        return flow(
            VehicleInfoMapper.merge_price_and_vehicle_data(vehicle_data, pricing_data),
            bind(VehicleInfoMapper.filter_response),
            bind(VehicleInfoMapper.map_response)
        )
