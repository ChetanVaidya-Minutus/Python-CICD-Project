provider "aws" {
   region = var.region
}


from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, Minutus Computing!!!!!"


if __name__ == "__main__":
    app.run()
