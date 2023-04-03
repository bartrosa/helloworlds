from flask import render_template, url_for, flash, redirect
from . import app


@app.route("/")
@app.route("/home")
def home():
    return render_template(
        'index.html'
    )


@app.route("/data")
def data():
    data = {
        "data": [
            {
                "id": "1",
                "desc": "dd",
                "type": "",
                "Test case no 1": "FAIL",
                "Test case no 2": "",
                "Test case no 3": "PASS",
                "Test case no 4": "",
                "Test case no 5": "BLOCKED"
            },
            {
                "id": "2",
                "desc": "dd",
                "type": "",
                "Test case no 1": "FAIL",
                "Test case no 2": "",
                "Test case no 3": "PASS",
                "Test case no 4": "",
                "Test case no 5": "N/A"
            },
            {
                "id": "3",
                "desc": "dd",
                "type": "",
                "Test case no 1": "FAIL",
                "Test case no 2": "",
                "Test case no 3": "PASS",
                "Test case no 4": "",
                "Test case no 5": "DESCOPED"
            }
    ]
}
    return data
