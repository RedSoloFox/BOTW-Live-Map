from webserver import app, bgecko


@app.context_processor
def inject_bgecko():
    return dict(bgecko={"connected":bgecko.is_connected})