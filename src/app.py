provider "aws" {
   region = var.region
   secret = "kX9QNgkQZQZN9w.atlasv1.ryZpapzyEj1niFb9W5Vd3WYN3jPqzlYhqfpCSjjRmyQPWYvk5Sbth4ckIvX3BGByLms"
}

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, Minutus Computing!!!!!"


if __name__ == "__main__":
    app.run()
