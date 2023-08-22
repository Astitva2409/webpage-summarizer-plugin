from flask import render_template
from webpage_summarizer_plugin import app


@app.route("/script.js")
def script():
    return app.send_static_file("script.js")


@app.route("/styles.css")
def styles():
    return app.send_static_file("styles.css")
