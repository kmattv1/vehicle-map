import React, { useState, useRef, useEffect } from "react";
import GoogleMapReact from "google-map-react";
import "./App.css";
import TopBar from "./components/TopBar";
import {AvailabilityCategory, clusterItemToMarker } from "./components/Marker";
import {getVehicleInformation, Point} from "./adapters/VehicleData";
import {GetClusterAndZoomFunction} from "./adapters/Cluster";

export type AppState = {
    loading: boolean;
    points: {
        available: Point[];
        reserved: Point[];
        disabled: Point[]
    };
}

export default function App() {
    const mapRef = useRef();
    const [bounds, setBounds] = useState([]);
    const [zoom, setZoom] = useState(10);
    const [appState, setAppState] = useState({
        loading: false,
        points: {available: [], reserved: [], disabled: []},
    } as AppState);

    const [selectedAvailability, setSelectedAvailability] = useState({
        availabilityFilter: "all"
    });

    useEffect(() => {
        setAppState({ loading: true, points: {available: [], reserved: [], disabled: []} });
        getVehicleInformation(selectedAvailability.availabilityFilter).then(markerPointsGroupedByVehicleAvailability => {
            setAppState({ loading: false, points: markerPointsGroupedByVehicleAvailability});
        })
    }, [setAppState, selectedAvailability, setSelectedAvailability]);

    const allPointCount = appState.points.available.length + appState.points.disabled.length + appState.points.reserved.length;

    const { clusters: availableClusters, zoom: availableZoomIn } = GetClusterAndZoomFunction(appState.points.available, mapRef, bounds, zoom);
    const { clusters: reservedClusters, zoom: reservedZoomIn } = GetClusterAndZoomFunction(appState.points.reserved, mapRef, bounds, zoom);
    const { clusters: disabledClusters, zoom: disabledZoomIn } = GetClusterAndZoomFunction(appState.points.disabled, mapRef, bounds, zoom);

    return (
        <div>
            <div style={{ height: "94vh", width: "100%", position: "absolute", top: 0 }}>
                <TopBar
                    onSelectorChange={(selectedAvailability: AvailabilityCategory) => {
                        // @ts-ignore
                        setSelectedAvailability({availabilityFilter: selectedAvailability});
                    }}
                />
            <GoogleMapReact
                bootstrapURLKeys={{ key: "" }}
                defaultCenter={{ lat: 52.5, lng: 13.34 }}
                defaultZoom={12}
                yesIWantToUseGoogleMapApiInternals
                onGoogleApiLoaded={({ map }) => {
                    mapRef.current = map;
                }}
                onChange={({ zoom, bounds }) => {
                    setZoom(zoom);
                    // @ts-ignore
                    setBounds([bounds.nw.lng, bounds.se.lat, bounds.se.lng, bounds.nw.lat]);
                }}
            >
                {availableClusters.map(cluster => clusterItemToMarker(cluster, allPointCount, "available", availableZoomIn))}
                {disabledClusters.map(cluster => clusterItemToMarker(cluster, allPointCount, "disabled", disabledZoomIn))}
                {reservedClusters.map(cluster => clusterItemToMarker(cluster, allPointCount, "reserved", reservedZoomIn))}
            </GoogleMapReact>
            </div>
        </div>
    );
}
