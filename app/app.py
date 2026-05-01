from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>CI/CD Pipeline - TFG ASIR</h1><p>Desplegado automaticamente con GitHub Actions, Docker y Helm</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
