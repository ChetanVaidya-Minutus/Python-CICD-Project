provider "aws" {
   region = var.region
   #shared_credentials_files = ["C:/Users/admin/.aws/credentials"]
   access_key = "AKIAT6OYGGM6Q2RGCKNG"
   secret_key = "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"
}


from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, Minutus Computing!!!!!"


if __name__ == "__main__":
    app.run()
