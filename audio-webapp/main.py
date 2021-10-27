#!/usr/bin/python3

from time import sleep
from os import system
from flask import Flask, render_template, request

def play_audio(file_name):
        system("gst-launch-1.0 filesrc location={} ! decodebin ! audioconvert ! autoaudiosink".format(file_name))

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
                play_audio(file_name = 'sound/a.mp3')
                return "A\n"

        elif state == 'B':
                play_audio(file_name = 'sound/b.mp3')
                return "B\n"

        elif state == 'C':
                play_audio(file_name = 'sound/c.mp3')
                return "C\n"

        elif state == 'D':
                play_audio(file_name = 'sound/d.mp3')
                return "D\n"
               
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)



