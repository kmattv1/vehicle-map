import useSupercluster from "use-supercluster";

export type ClusterWithZoom = {
    clusters: any[];
    zoom: (clusterId: string, lat: number, lng: number) => void;
}

// @ts-ignore
export function GetClusterAndZoomFunction(points, mapRef, bounds, zoom): ClusterWithZoom {
    const { clusters, supercluster: availableSuperCluster } = useSupercluster({
        points,
        bounds,
        zoom,
        options: { radius: 75, maxZoom: 20 }
    });

    const zoomIn = (clusterId: string, lat: number, lng: number) => {
        try {
            const expansionZoom = Math.min(
                availableSuperCluster.getClusterExpansionZoom(clusterId),
                20
            );
            // @ts-ignore
            mapRef.current.setZoom(expansionZoom);
            // @ts-ignore
            mapRef.current.panTo({lat, lng});
        } catch (e){
            console.error(e);
        }
    };

    return {
        clusters,
        zoom: zoomIn
    }
}
