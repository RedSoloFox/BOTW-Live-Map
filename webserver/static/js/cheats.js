function rest(url) {
    var xhttp = new XMLHttpRequest();
    xhttp.open("GET", url, false);
    xhttp.send();
    //return xhttp.responseText
    return JSON.parse(xhttp.responseText);
} // Replace this with a shared thing?

// Post
function post_rest(url, params) {
    var xhttp = new XMLHttpRequest();
    xhttp.open("POST", url, false);
    xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhttp.send(params);
    //return xhttp.responseText
    return JSON.parse(xhttp.responseText);
} // Replace this with a shared thing?

// Start here

function set_health() {
    console.log('set_health');
    // set health here
    h_input = document.getElementById("health_select").value * 4;
    console.log(h_input);
    post_rest('/api/cheats/health/', `health=${h_input}`);
}

function get_health() {
    console.log('get_health');
    // Each heart == 4 health, simple enough
    health = rest("/api/cheats/health/")["health"];
    health_div = document.getElementById("current_health");
    // Show health in hearts
    health_div.innerHTML = `Hearts: ${health[0]/4}/${health[1]/4}`;
}

function set_stamina() {
    console.log('set_stamina');
    // set stamina
}

function get_stamina() {
    console.log('get_stamina');
    // get stamina
    stamina = rest('/api/cheats/stamina/')['stamina'];
    stamina_div = document.getElementById('current_stamina');
    stamina_div.innerHTML = `Stamina: ${stamina}`;
}

function set_rupees() {
    console.log('set_rupees');
    // set rupees
}

function get_rupees() {
    console.log('get_rupees');
    // get rupees
    rupees = rest('/api/cheats/rupees/')['rupees'];
    rupee_div = document.getElementById('show_rupees');
    rupee_div.innerHTML = `Rupees: ${rupees}`
}

function set_mon() {
    console.log('set_mon');
    // set mon
}

function get_mon() {
    console.log('get_mon');
    // get mon
}

function set_speed() {
    console.log('set_speed');
    // set speed
}

function set_damage() {
    console.log('set_damage');
    // set damage
}

function set_weather() {
    console.log('set_weather');
    // set weather
}

function set_time() {
    console.log('set_time');
    // set time
}

function set_abilities() {
    console.log('set_abilities');
    // set abilities
}