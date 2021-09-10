import {AvailabilityCategory} from "../components/Marker";

export type Point =
    {
        type: "Feature";
        properties: {
            cluster: boolean;
            vehicleId: string;
            type: string;
            availabilityCategory: string;
        };
        geometry: {
            type: "Point";
            coordinates: number[];
        };
    };

export type Vehicle = {
    id: string;
    lat: string;
    lon: string;
    vehicle_type_id: string;
    pricing_description: string
};

export type MarkerPointsGroupedByVehicleAvailability = {
    available: Point[];
    disabled: Point[];
    reserved: Point[];
}

export async function getVehicleInformation(availabilityFilter: string = "all"): Promise<MarkerPointsGroupedByVehicleAvailability> {
    const apiUrl = `/vehicles?group=${availabilityFilter}`;
    return await fetch(apiUrl).then((res) => res.json()).then((data) => {
        const available = vehicleListToPintList(data.available ?? [], "available");
        const reserved = vehicleListToPintList(data.reserved ?? [], "reserved");
        const disabled = vehicleListToPintList(data.disabled ?? [], "disabled");
        return {
            reserved,
            available,
            disabled
        }
    })
}

function vehicleListToPintList(vehicles: Vehicle[], availabilityCategory: AvailabilityCategory): Point[]{
    return vehicles.map((vehicle: Vehicle) => ({
        type: "Feature",
        properties: {
            cluster: false,
            vehicleId: vehicle.id,
            type: vehicle.vehicle_type_id,
            availabilityCategory
        },
        geometry: {
            type: "Point",
            coordinates: [
                parseFloat(vehicle.lon),
                parseFloat(vehicle.lat)
            ]
        }
    }));
}
