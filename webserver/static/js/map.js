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
    // set up the map
	map = new L.Map('map');

	// create the tile layer with correct attribution
	var osmUrl='http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
	var osmAttrib='Map data © <a href="http://openstreetmap.org">OpenStreetMap</a> contributors';
	var osm = new L.TileLayer(osmUrl, {minZoom: 8, maxZoom: 12, attribution: osmAttrib});

	// start the map in South-East England
	map.setView(new L.LatLng(51.3, 0.7),9);
	map.addLayer(osm);
	console.log("Map initialized")
}