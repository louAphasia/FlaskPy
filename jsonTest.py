import json
from flask import make_response, Flask

app =Flask(__name__)
@app.route('/json')
def get_image():
    response= make_response(json.dumps({"foo":"bar"}))
    response.mimetype='application/json'
    return response

if __name__=="__main__":
    app.run(debug=True)