const yigo = L.marker([13.5640, 144.9061]).bindPopup('Yigo'),
    dededo = L.marker([13.5453, 144.8511]).bindPopup('Dededo'),
    mangilao = L.marker([13.4702, 144.8456]).bindPopup('Mangilao'),
    tamuning = L.marker([13.5005, 144.7956]).bindPopup('Tamuning'), 
    barrigada = L.marker([13.4708, 144.8181]).bindPopup('Barrigada'),
    agana = L.marker([13.4763, 144.7502]).bindPopup('Agana'), 
    asan = L.marker([13.4608, 144.7247]).bindPopup('Asan'), 
    piti = L.marker([13.4456, 144.6918]).bindPopup('Piti'),
    yona = L.marker([13.4010, 144.7522]).bindPopup('Yona'),
    santaRita = L.marker([13.3743, 144.7083]).bindPopup('Santa Rita')
    agat = L.marker([13.3673, 144.6643]).bindPopup('Agat'),
    talofofo = L.marker([13.3383, 144.7302]).bindPopup('Talofofo'),
    inarajan = L.marker([13.2792, 144.7302]).bindPopup('Inajaran'),
    umatac = L.marker([13.3139, 144.6698]).bindPopup('Umatac'),
    merizo = L.marker([13.2682, 144.6918]).bindPopup('Merizo'); 

fetch(urlWellsGeoJSON)
    .then(response => response.json())
    .then(geojson => {
        function getWellValues(feature, layer) {
            if (feature.properties) {
                layer.bindPopup(`Well: ${feature.properties.Well} <br> Lat: ${feature.properties.LAT} <br> Lon: ${feature.properties.LON} <br> Sig: ${feature.properties.Sig}`);
            }
        }
        const wellGeoJSON = L.geoJSON(geojson, {onEachFeature: getWellValues}).addTo(map);
    })

const villages = L.layerGroup([yigo, dededo, mangilao, tamuning, barrigada, agana, asan, piti, yona, santaRita, agat, talofofo, inarajan, umatac, merizo]); 

const osm = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
maxZoom: 19,
attribution: '© OpenStreetMap'
});

const map = L.map('map', {
center: [13.525293719720237, 144.85456459772948], 
zoom: 13,
layers: [osm, villages]
});

const baseLayers = { 
    'Open Street Map': osm
}; 

const overlays = {
    'Villages': villages
};

const layerControl = L.control.layers({"Open Street Map": osm}).addTo(map);