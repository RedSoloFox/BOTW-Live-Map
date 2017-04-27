// Global Vars
var stopped = false;
var map, ajaxRequest, plotList;
var plotLayers=[];

function rest(url) {
    var xhttp = new XMLHttpRequest();
    xhttp.open("GET", url, false);
    xhttp.setRequestHeader("Content-type", "application/json");
    xhttp.send();
    //return xhttp.responseText
    return JSON.parse(xhttp.responseText);
}

function coordinates_test() {
    coordinates = document.getElementById("coordinates");
    rrr = rest("/api/coordinates/")['coordinates'];
    coor_x = rrr['x'], coor_y = rrr['y'], coor_z = rrr['z'];
    coordinates.innerHTML = `X: ${coor_x}, Y: ${coor_y}, Z: ${coor_z}`;
    console.log(rrr);
}

function coord_loop() {
    coordinates_test();
    if (!stopped) {
        console.log(stopped);
        setTimeout(coord_loop, 500)
    } else {
        stopped = false;
    }
}

function stop_coord_loop() {
    stopped = true;
    console.log('stop')
}

function initMap() {
    console.log("init")
	map = new L.Map('map');
    L.tileLayer('/static/img/tiles/{z}/{x}/{y}.png', {minZoom: 3, maxZoom: 6, attribution: 'RedSoloFox'}).addTo(map);

    //Set center of screen ((lat, long), zoom)
    map.setView(new L.LatLng(50, 50),0);
	map.addLayer(osm);
	console.log("Map initialized")
}