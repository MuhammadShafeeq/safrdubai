from SafrDubai import app
from flask import render_template, request, redirect, flash, url_for
from SafrDubai.ApiHandler import geocode, transit
import json
from datetime import datetime, timezone

@app.route('/route', methods=["GET", "POST"])
def route():
    if request.method == "POST":
        starting_point = request.form["starting"]
        destination = request.form["destination"]
        starting_point = geocode(starting_point)
        destination = geocode(destination)
        if starting_point == "An Error Occurred":
            flash("Unable to find route", "failure")
            return render_template("form.html")
        else:
            route = transit(starting_point[0], starting_point[1], destination[0], destination[1])
            try:
                if route["notices"][0]["code"] == "noCoverage":
                    flash("Routing is not possible due to missing information. (Try again with full address)")
                    return render_template("form.html")
            except:
                return render_template("transit.html", route=route)

    return render_template('form.html')

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")