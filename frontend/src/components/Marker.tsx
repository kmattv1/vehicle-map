import React from 'react';
import {assertNever} from "../utils";

export type AvailabilityCategory = "available" | "reserved" | "disabled";

export type MarkerCluster = {
    id: string;
    pointCount: number;
    availabilityCategory: AvailabilityCategory;
}

export type Cluster = {
    id: string;
    geometry: {
        coordinates: number[];
    };
    properties: {
        point_count: number;
        vehicleId: string;
    };
}

export interface MapMarkerProps {
    key: string;
    lat: number;
    lng: number;
    cluster: MarkerCluster;
    allPointsCount: number;
    onClick: (clusterId: string, lat: number, lng: number) => void;
}

function getDeviceClass(availabilityCategory: AvailabilityCategory): string {
    switch (availabilityCategory) {
        case "available":
            return "available-vehicle-marker";
        case "disabled":
            return "disabled-vehicle-marker";
        case "reserved":
            return "reserved-vehicle-marker";
        default:
            assertNever(availabilityCategory)
    }
}

export function clusterItemToMarker(cluster: Cluster, allPointsCount: number, availabilityCategory:AvailabilityCategory, onClick: (clusterId: string, lat: number, lng: number) => void) {
    const [longitude, latitude] = cluster.geometry.coordinates;
    const {point_count: pointCount} = cluster.properties;

    const markerCluster: MarkerCluster = {
        id: cluster.id ?? cluster.properties.vehicleId,
        pointCount: pointCount ?? 1,
        availabilityCategory,
    };


    return (<Marker
            key={`${availabilityCategory}-${markerCluster.id}`}
            lat={latitude}
            lng={longitude}
            cluster={markerCluster}
            allPointsCount={allPointsCount}
            onClick={onClick}
        />
    );
}

export const Marker = (props: MapMarkerProps) => {
    const {cluster, allPointsCount, onClick, lat, lng} = props;
    const onClickAction = cluster.pointCount > 1 ? () => onClick(cluster.id, lat, lng) : ()=>{};

    return (
        <div
            className={getDeviceClass(cluster.availabilityCategory)}
            style={{
                width: `${4 + (cluster.pointCount / allPointsCount) * 200}px`,
                height: `${4 + (cluster.pointCount / allPointsCount) * 200}px`
            }}
            onClick={onClickAction}
        >
            {cluster.pointCount}
        </div>
    )
}
