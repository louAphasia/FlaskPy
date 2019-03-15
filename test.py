from flask import Flask, request

app=Flask(__name__)
@app.route('/')
def root():
    return "Request path is:" + request.path

@app.route('/test/')
def test():
    return "Request path is " + request.path

if __name__=="__main__":
    app.run(debug=True)