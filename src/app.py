from flask import Flask, request, jsonify,render_template
import pickle
import pandas as pd
import os

# Crear la aplicación Flask
app = Flask(__name__)

# Ruta segura al modelo entrenado
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, '..', 'models', 'model.pkl')

# Cargar el modelo entrenado
try:
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)
    print("✅ Modelo cargado correctamente.")
except FileNotFoundError:
    print(f"❌ No se encontró el modelo en {MODEL_PATH}.")
    model = None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({"error": "El modelo no está cargado."}), 500

    try:
        # Recibir JSON
        data = request.get_json()

        # Convertir a DataFrame
        df = pd.DataFrame([data])

        # Verificar columnas requeridas
        required_cols = ['Open', 'High', 'Low', 'Volume', 'MA_7']
        if not all(col in df.columns for col in required_cols):
            return jsonify({
                "error": "Faltan columnas en los datos. Se requieren: " + ', '.join(required_cols)
            }), 400

        # Predecir
        prediction = model.predict(df)[0]

        return jsonify({
            "predicted_price": float(prediction)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)


  