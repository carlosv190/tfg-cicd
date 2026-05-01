from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route("/")
def home():
    hostname = socket.gethostname()
    return """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TFG ASIR - CI/CD Pipeline</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }

        body {
            font-family: 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
            min-height: 100vh;
            color: white;
            padding: 40px 20px;
        }

        .container { max-width: 900px; margin: 0 auto; }

        .header {
            text-align: center;
            margin-bottom: 50px;
            animation: fadeIn 1s ease;
        }

        .header h1 {
            font-size: 2.8em;
            background: linear-gradient(90deg, #00c9ff, #92fe9d);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 10px;
        }

        .header p {
            color: #aaa;
            font-size: 1.1em;
        }

        .badge {
            display: inline-block;
            background: #00c9ff22;
            border: 1px solid #00c9ff55;
            color: #00c9ff;
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.85em;
            margin-top: 10px;
        }

        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }

        .card {
            background: rgba(255,255,255,0.05);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 16px;
            padding: 25px;
            backdrop-filter: blur(10px);
            transition: transform 0.3s, border-color 0.3s;
            animation: slideUp 0.6s ease;
        }

        .card:hover {
            transform: translateY(-5px);
            border-color: #00c9ff55;
        }

        .card .icon { font-size: 2.5em; margin-bottom: 15px; }
        .card h3 { font-size: 1.1em; color: #00c9ff; margin-bottom: 8px; }
        .card p { color: #ccc; font-size: 0.9em; line-height: 1.5; }

        .pipeline {
            background: rgba(255,255,255,0.03);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 16px;
            padding: 30px;
            margin-bottom: 30px;
        }

        .pipeline h2 {
            text-align: center;
            margin-bottom: 30px;
            color: #92fe9d;
            font-size: 1.3em;
        }

        .steps {
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 10px;
        }

        .step {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 8px;
            flex: 1;
            min-width: 80px;
        }

        .step .circle {
            width: 55px;
            height: 55px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.5em;
            border: 2px solid #00c9ff44;
            background: #00c9ff11;
        }

        .step span {
            font-size: 0.75em;
            color: #aaa;
            text-align: center;
        }

        .arrow { color: #00c9ff55; font-size: 1.5em; flex: 0; }

        .info-bar {
            background: rgba(0,201,255,0.08);
            border: 1px solid rgba(0,201,255,0.2);
            border-radius: 12px;
            padding: 20px 30px;
            display: flex;
            justify-content: space-around;
            flex-wrap: wrap;
            gap: 15px;
        }

        .info-item { text-align: center; }
        .info-item .label { color: #aaa; font-size: 0.8em; margin-bottom: 5px; }
        .info-item .value { color: #00c9ff; font-size: 1em; font-weight: bold; font-family: monospace; }

        .status-dot {
            display: inline-block;
            width: 10px;
            height: 10px;
            background: #92fe9d;
            border-radius: 50%;
            margin-right: 6px;
            animation: pulse 2s infinite;
        }

        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.3; }
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        @keyframes slideUp {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
</head>
<body>
    <div class="container">

        <div class="header">
            <h1>⚙️ CI/CD Pipeline</h1>
            <p>Trabajo de Fin de Grado · ASIR Y CON MUESTRA COMPLETADA</p>
            <span class="badge"><span class="status-dot"></span>Aplicación desplegada y en ejecución</span>
        </div>

        <div class="grid">
            <div class="card">
                <div class="icon">🐙</div>
                <h3>GitHub Actions</h3>
                <p>Pipeline automatizada que se dispara con cada push a la rama main.</p>
            </div>
            <div class="card">
                <div class="icon">🐳</div>
                <h3>Docker</h3>
                <p>La imagen de la aplicación se construye y publica automáticamente en DockerHub.</p>
            </div>
            <div class="card">
                <div class="icon">⛵</div>
                <h3>Helm</h3>
                <p>Gestiona el despliegue en Kubernetes mediante charts parametrizables.</p>
            </div>
            <div class="card">
                <div class="icon">☸️</div>
                <h3>Kubernetes</h3>
                <p>Orquesta los contenedores garantizando disponibilidad y escalabilidad.</p>
            </div>
        </div>

        <div class="pipeline">
            <h2>🔄 Flujo de la Pipeline</h2>
            <div class="steps">
                <div class="step">
                    <div class="circle">📝</div>
                    <span>Push a GitHub</span>
                </div>
                <div class="arrow">→</div>
                <div class="step">
                    <div class="circle">⚙️</div>
                    <span>GitHub Actions</span>
                </div>
                <div class="arrow">→</div>
                <div class="step">
                    <div class="circle">🐳</div>
                    <span>Build Docker</span>
                </div>
                <div class="arrow">→</div>
                <div class="step">
                    <div class="circle">📦</div>
                    <span>Push DockerHub</span>
                </div>
                <div class="arrow">→</div>
                <div class="step">
                    <div class="circle">⛵</div>
                    <span>Helm Deploy</span>
                </div>
                <div class="arrow">→</div>
                <div class="step">
                    <div class="circle">✅</div>
                    <span>App en K8s</span>
                </div>
            </div>
        </div>

        <div class="info-bar">
            <div class="info-item">
                <div class="label">Pod</div>
                <div class="value">""" + hostname + """</div>
            </div>
            <div class="info-item">
                <div class="label">Orquestador</div>
                <div class="value">Kubernetes</div>
            </div>
            <div class="info-item">
                <div class="label">Gestor de despliegue</div>
                <div class="value">Helm v3</div>
            </div>
            <div class="info-item">
                <div class="label">Registro de imágenes</div>
                <div class="value">DockerHub</div>
            </div>
        </div>

    </div>
</body>
</html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
