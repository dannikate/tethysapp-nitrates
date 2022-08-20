const map = L.map('map', {
    center: [13.455207, 144.7900861],
    zoom: 11,
});
const osm = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '© OpenStreetMap'
}).addTo(map);
const baseLayers = {
    'Open Street Map': osm
};

const yigo = L.marker([13.5640, 144.9061]).bindPopup('Yigo')
const dededo = L.marker([13.5453, 144.8511]).bindPopup('Dededo')
const mangilao = L.marker([13.4702, 144.8456]).bindPopup('Mangilao')
const tamuning = L.marker([13.5005, 144.7956]).bindPopup('Tamuning')
const barrigada = L.marker([13.4708, 144.8181]).bindPopup('Barrigada')
const agana = L.marker([13.4763, 144.7502]).bindPopup('Agana')
const asan = L.marker([13.4608, 144.7247]).bindPopup('Asan')
const piti = L.marker([13.4456, 144.6918]).bindPopup('Piti')
const yona = L.marker([13.4010, 144.7522]).bindPopup('Yona')
const santaRita = L.marker([13.3743, 144.7083]).bindPopup('Santa Rita')
const agat = L.marker([13.3673, 144.6643]).bindPopup('Agat')
const talofofo = L.marker([13.3383, 144.7302]).bindPopup('Talofofo')
const inarajan = L.marker([13.2792, 144.7302]).bindPopup('Inajaran')
const umatac = L.marker([13.3139, 144.6698]).bindPopup('Umatac')
const merizo = L.marker([13.2682, 144.6918]).bindPopup('Merizo')

const villages = L.layerGroup([yigo, dededo, mangilao, tamuning, barrigada, agana, asan, piti, yona, santaRita, agat, talofofo, inarajan, umatac, merizo]);

const overlays = {
    'Villages': villages
};

const layerControl = L.control.layers(baseLayers, overlays).addTo(map);

const plotWNL = (plotData, selectedWellID) => {
    const wnlTrace1 = {
        x: plotData.datetime,
        y: plotData.values,
        type: 'scatter',
        mode: 'markers',
        name: 'Well Nitrate Levels'
    }
    const layout = { 
        title: {
            text: `Nitrate Levels for Well ${selectedWellID}`,
            font: {
                size: 20
            }
        },
        xaxis: {
            title: "Years", 
        },
        yaxis: {
            title: 'ppm (mg/L)',
        }
    }
    Plotly.newPlot('plot-div', [wnlTrace1], layout)
}

fetch(urlWellsGeoJSON)
    .then(response => response.json())
    .then(geojson => {
        function getWellValues(feature, layer) {
            if (feature.properties) {
                layer.bindPopup(`Well: ${feature.properties.Well} <br> Lat: ${feature.properties.LAT} <br> Lon: ${feature.properties.LON} <br> Sig: ${feature.properties.Sig}
                `);
            }
            layer.on('click', a => getNitrateTimeSeries(a.target.feature.properties.Well))
        }
        const wellGeoJSON = L.geoJSON(geojson, {onEachFeature: getWellValues}).addTo(map);
        layerControl.addOverlay(wellGeoJSON, "Well Locations")
    })

const getNitrateTimeSeries = (selectedWellID) => {
    fetch(urlGetNitrateTimeSeries + `?well_id=${selectedWellID}`)
        .then(response => response.json())
        .then(plotData => {
            plotWNL(plotData, selectedWellID)
            document.getElementById("stats-div").innerText = JSON.stringify(plotData.stats, null, 3)
        })
}

// const getWellStats = (selectedWellID) => {
//     fetch(urlGetWellStats + `?well_id=${selectedWellID}`)
//         .then(response => response.json())
//         .then(wellStats => {
//             // document.getElementById("stats-div").innerHTML += plotData.stats.Average
//             console.log(wellStats);
//         })
// }