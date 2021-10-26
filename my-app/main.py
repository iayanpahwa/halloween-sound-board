#!/usr/bin/python3

from time import sleep
from os import system
from flask import Flask, render_template, request

app = Flask(__name__)

# Load the main form template on webrequest for the root page
@app.route("/")

def main():

    # Create a template data dictionary to send any data to the template
    templateData = {
        'title' : 'halloween sound board'
        }
    # Pass the template data into the template powrcycle.html and return it to the user
    return render_template('index.html', **templateData)

@app.route("/play/<state>")
def action_play(state):
        if state == 'A':
                system("gst-launch-1.0 filesrc location={} ! decodebin ! audioconvert ! autoaudiosink".format("sound/a.mp3"))
                return "A\n"
                
        elif state == 'B':
                system("gst-launch-1.0 filesrc location={} ! decodebin ! audioconvert ! autoaudiosink".format("sound/b.mp3"))
                return "B\n"

        elif state == 'C':
                system("gst-launch-1.0 filesrc location={} ! decodebin ! audioconvert ! autoaudiosink".format("sound/c.mp3"))
                return "C\n"

        elif state == 'D':
                system("gst-launch-1.0 filesrc location={} ! decodebin ! audioconvert ! autoaudiosink".format("sound/d.mp3"))
                return "D\n"
               
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)



