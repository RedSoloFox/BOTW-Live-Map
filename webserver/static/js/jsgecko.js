function post(path, params, method) {
    method = method || "post"; // Set method to post by default if not specified.

    // The rest of this code assumes you are not using a library.
    // It can be made less wordy if you use one.
    var form = document.createElement("form");
    form.setAttribute("method", method);
    form.setAttribute("action", path);

    for(var key in params) {
        if(params.hasOwnProperty(key)) {
            var hiddenField = document.createElement("input");
            hiddenField.setAttribute("type", "hidden");
            hiddenField.setAttribute("name", key);
            hiddenField.setAttribute("value", params[key]);

            form.appendChild(hiddenField);
         }
    }

    document.body.appendChild(form);
    form.submit();
}

function gecko_disconnect() {
    console.log("Disconnection from Wii U")
    post("/api/connect/", {"cord":"disconnect"})
    console.log("Disconnected")
}

function gecko_connect(ip) {
    console.log("Connecting to: " + ip)
    post("/api/connect/", {"cord":"connect", "ip":ip})
    console.log("Attempted Connect")
}