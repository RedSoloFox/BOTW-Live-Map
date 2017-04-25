// Global Vars
var stopped = false;

function rest(url) {
    var xhttp = new XMLHttpRequest();
    xhttp.open("GET", url, false);
    xhttp.setRequestHeader("Content-type", "application/json");
    xhttp.send();
    return xhttp.responseText
    //return JSON.parse(xhttp.responseText);
}

function coordinates_test() {
    coordinates = document.getElementById("coordinates");
    console.log("A");
    rrr = rest("/api/coordinates/");
    coordinates.innerHTML = rrr;
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