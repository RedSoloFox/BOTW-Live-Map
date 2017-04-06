
function initMap() {
    console.log("Fack")
    var map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: 0, lng: 0},
        zoom: 1,
        streetViewControl: false
    })
    console.log("init map")
}