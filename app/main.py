import os
from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hurray Cogratulations Succesfully Created CI/CD PIPELINE</h1>"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
