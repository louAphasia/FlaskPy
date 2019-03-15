from flask import Flask, app


@app.route('/data', methods=['GET'])
def show_data():

@app.route('/data', methods=['POST'])
def handle_data():

@app.route('/user/<username>')
def greet(username):
    return "Hello" +username