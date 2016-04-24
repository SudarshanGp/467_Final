from flask import Flask, render_template, request, jsonify, send_from_directory, redirect, url_for
import radar_parser
import os, sys
app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    # radar_parser.parse_file("static/res/nihal.csv")
    return render_template('base.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
