from flask import Flask

app= Flask(__name__)


@app.route("/")
def home():
    return "hello from performance test"


@app.route("/health")
def home():
    return {"status": "ok"}

if __name__=="__main__" :
    app.route(host="0.0.0.0", port=5000)


    