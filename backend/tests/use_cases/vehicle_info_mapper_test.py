import unittest

from src.use_cases.vehicle_info_mapper import VehicleInfoMapper


class TestVehicleInfoMapper(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_disabled_mapping(self):
        # Given
        plans = [
            {"plan_id": "c98e70e6-5f48-4b14-be64-b6e933656497", "name": "scooter-standard-pricing-berlin",
             "currency": "EUR", "price": 1, "is_taxable": False,
             "description": "Standard pricing for scooters, 1.00 EUR to unlock, 0.19 EUR per minute to rent",
             "per_min_pricing": [{"start": 0, "rate": 0.19, "interval": 1}]}]
        bikes = [{"bike_id": "89cb120fa4c1703709b52a5e0584ca47651c6ba7aa7c4299711cd0ae15470b11", "lat": 43.493509,
                  "lon": 39.989879, "is_reserved": False, "is_disabled": True, "vehicle_type_id": "escooter",
                  "current_range_meters": 0, "pricing_plan_id": "c98e70e6-5f48-4b14-be64-b6e933656497",
                  "rental_uris": {"android": "https://tier.page.link/Vbaff", "ios": "https://tier.page.link/Vbaff"}}]

        # When
        mapped_data = VehicleInfoMapper.group_and_map_data(bikes, plans).unwrap()

        # Then
        expected_result = {
            "available": [],
            "reserved": [],
            "disabled": [{
                "id": "89cb120fa4c1703709b52a5e0584ca47651c6ba7aa7c4299711cd0ae15470b11",
                "lat": 43.493509,
                "lon": 39.989879,
                "vehicle_type_id": "escooter",
                "pricing_description": "Standard pricing for scooters, 1.00 EUR to unlock, 0.19 EUR per minute to rent"
            }]}

        self.assertEqual(mapped_data.disabled[0].id, expected_result["disabled"][0]["id"])
        self.assertEqual(mapped_data.disabled[0].lat, expected_result["disabled"][0]["lat"])
        self.assertEqual(mapped_data.disabled[0].lon, expected_result["disabled"][0]["lon"])
        self.assertEqual(mapped_data.disabled[0].vehicle_type_id, expected_result["disabled"][0]["vehicle_type_id"])
        self.assertEqual(mapped_data.disabled[0].pricing_description,
                         expected_result["disabled"][0]["pricing_description"])

    def test_available_mapping(self):
        # Given
        plans = [
            {"plan_id": "c98e70e6-5f48-4b14-be64-b6e933656497", "name": "scooter-standard-pricing-berlin",
             "currency": "EUR", "price": 1, "is_taxable": False,
             "description": "Standard pricing for scooters, 1.00 EUR to unlock, 0.19 EUR per minute to rent",
             "per_min_pricing": [{"start": 0, "rate": 0.19, "interval": 1}]}]
        bikes = [{"bike_id": "89cb120fa4c1703709b52a5e0584ca47651c6ba7aa7c4299711cd0ae15470b11", "lat": 43.493509,
                  "lon": 39.989879, "is_reserved": False, "is_disabled": False, "vehicle_type_id": "escooter",
                  "current_range_meters": 0, "pricing_plan_id": "c98e70e6-5f48-4b14-be64-b6e933656497",
                  "rental_uris": {"android": "https://tier.page.link/Vbaff", "ios": "https://tier.page.link/Vbaff"}}]

        # When
        mapped_data = VehicleInfoMapper.group_and_map_data(bikes, plans).unwrap()

        # Then
        expected_result = {
            "available": [{
                "id": "89cb120fa4c1703709b52a5e0584ca47651c6ba7aa7c4299711cd0ae15470b11",
                "lat": 43.493509,
                "lon": 39.989879,
                "vehicle_type_id": "escooter",
                "pricing_description": "Standard pricing for scooters, 1.00 EUR to unlock, 0.19 EUR per minute to rent"
            }],
            "reserved": [],
            "disabled": []}

        self.assertEqual(mapped_data.available[0].id, expected_result["available"][0]["id"])
        self.assertEqual(mapped_data.available[0].lat, expected_result["available"][0]["lat"])
        self.assertEqual(mapped_data.available[0].lon, expected_result["available"][0]["lon"])
        self.assertEqual(mapped_data.available[0].vehicle_type_id, expected_result["available"][0]["vehicle_type_id"])
        self.assertEqual(mapped_data.available[0].pricing_description,
                         expected_result["available"][0]["pricing_description"])

    def test_reserved_mapping(self):
        # Given
        plans = [
            {"plan_id": "c98e70e6-5f48-4b14-be64-b6e933656497", "name": "scooter-standard-pricing-berlin",
             "currency": "EUR", "price": 1, "is_taxable": False,
             "description": "Standard pricing for scooters, 1.00 EUR to unlock, 0.19 EUR per minute to rent",
             "per_min_pricing": [{"start": 0, "rate": 0.19, "interval": 1}]}]
        bikes = [{"bike_id": "89cb120fa4c1703709b52a5e0584ca47651c6ba7aa7c4299711cd0ae15470b11", "lat": 43.493509,
                  "lon": 39.989879, "is_reserved": True, "is_disabled": False, "vehicle_type_id": "escooter",
                  "current_range_meters": 0, "pricing_plan_id": "c98e70e6-5f48-4b14-be64-b6e933656497",
                  "rental_uris": {"android": "https://tier.page.link/Vbaff", "ios": "https://tier.page.link/Vbaff"}}]

        # When
        mapped_data = VehicleInfoMapper.group_and_map_data(bikes, plans).unwrap()

        # Then
        expected_result = {
            "available": [],
            "reserved": [{
                "id": "89cb120fa4c1703709b52a5e0584ca47651c6ba7aa7c4299711cd0ae15470b11",
                "lat": 43.493509,
                "lon": 39.989879,
                "vehicle_type_id": "escooter",
                "pricing_description": "Standard pricing for scooters, 1.00 EUR to unlock, 0.19 EUR per minute to rent"
            }],
            "disabled": []}

        self.assertEqual(mapped_data.reserved[0].id, expected_result["reserved"][0]["id"])
        self.assertEqual(mapped_data.reserved[0].lat, expected_result["reserved"][0]["lat"])
        self.assertEqual(mapped_data.reserved[0].lon, expected_result["reserved"][0]["lon"])
        self.assertEqual(mapped_data.reserved[0].vehicle_type_id, expected_result["reserved"][0]["vehicle_type_id"])
        self.assertEqual(mapped_data.reserved[0].pricing_description,
                         expected_result["reserved"][0]["pricing_description"])


if __name__ == '__main__':
    unittest.main()
