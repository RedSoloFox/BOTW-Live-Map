// Global Vars
var stopped = false;
var map, rc, playerMarker;

// heart icon
var heartIcon = L.icon({
    iconUrl: '/static/img/markers/heart.png',

    iconSize:     [30, 30], // size of the icon
    iconAnchor:   [15, 30], // point of the icon which will correspond to marker's location
    popupAnchor:  [-1, -26] // point from which the popup should open relative to the iconAnchor
});

function rest(url) {
    var xhttp = new XMLHttpRequest();
    xhttp.open("GET", url, false);
    xhttp.send();
    //return xhttp.responseText
    return JSON.parse(xhttp.responseText);
}

function initMap() {
    console.log("Start Map Init");
    // Setup Map
    var img = [24000, 20000];
    map = new L.Map('map');

    // Change Icon dir
    L.Icon.Default.imagePath = "/static/img/markers/";

    // setup custom map details
    rc = new L.RasterCoords(map, img);
    map.setMaxZoom(rc.zoomLevel());
    map.setView(rc.unproject([img[0], img[1]]), 2);

    // Set marker on click
    /*
    map.on('click', function (event) {
        var coords = rc.project(event.latlng);
        console.log(coords);
        var marker = L.marker(rc.unproject(coords), {icon: heartIcon}).addTo(map);
        marker.bindPopup('[' + Math.floor(coords.x) + ',' + Math.floor(coords.y) + ']')
            .openPopup()
    });
    */

    L.tileLayer('/static/img/tiles/{z}/{x}/{y}.png', {noWrap: true}).addTo(map);
    // Create marker
    current_location = rest("/api/coordinates/")["coordinates"];
    loc = [parseFloat(current_location['x']), parseFloat(current_location['y'])];
    playerMarker = L.marker(rc.unproject(loc), {icon: heartIcon}).addTo(map);

    console.log("Map initialized")
}

function update_Marker() {
    current_location = rest("/api/coordinates/")["coordinates"];
    loc = [parseFloat(current_location['x']), parseFloat(current_location['y'])];
    playerMarker.setLatLng(rc.unproject(loc))
}
function marker_update_loop() {
    update_Marker();
    if (!stopped) {
        setTimeout(marker_update_loop, 3000)
    } else {
        stopped = false;
    }
}

function stop_update_loop() {
    stopped = true;
    console.log('stop')
}