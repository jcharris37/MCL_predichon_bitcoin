# run_pipeline.py

from data_fetching import fetch_btc_data
from data_preprocessing import preprocess_data
from model_training import train_model
import pandas as pd
import os
import pickle
import matplotlib.pyplot as plt

# 1. Crear carpetas necesarias
os.makedirs('data', exist_ok=True)
os.makedirs('models', exist_ok=True)

# 2. Descargar datos actualizados de BTC
print("📥 Descargando datos...")
btc_data = fetch_btc_data()
btc_data.to_csv('data/bitcoin_data.csv')
print("✅ Datos guardados en data/bitcoin_data.csv")

# 3. Preprocesar los datos
print("⚙️ Preprocesando datos...")
preprocessed_data = preprocess_data(btc_data)
preprocessed_data.to_csv('data/preprocessed_data.csv', index=False)
print("✅ Datos preprocesados guardados en data/preprocessed_data.csv")

# 4. Verificar si los datos están listos para entrenar
required_cols = ['Open', 'High', 'Low', 'Volume', 'MA_7', 'Close']
missing_cols = [col for col in required_cols if col not in preprocessed_data.columns]

if missing_cols:
    print(f"❌ No se puede entrenar el modelo. Faltan columnas: {missing_cols}")
elif preprocessed_data.empty:
    print("❌ No hay datos disponibles después del preprocesamiento.")
else:
    print("🤖 Entrenando el modelo...")
    try:
        model, y_test, y_pred = train_model(preprocessed_data)

        # 5. Guardar el modelo entrenado
        with open('models/model.pkl', 'wb') as f:
            pickle.dump(model, f)
        print("✅ Modelo guardado en models/model.pkl")

        # 6. Graficar resultados y guardar imagen
        plt.figure(figsize=(10, 5))
        plt.plot(y_test.values, label='Real', color='blue')
        plt.plot(y_pred, label='Predicho', color='red')
        plt.title("📈 Precio Real vs Predicho (normalizado)")
        plt.xlabel("Índice de muestra")
        plt.ylabel("Precio de cierre (normalizado)")
        plt.legend()
        plt.tight_layout()
        plt.savefig("models/grafico.png")  # Guardar imagen
        plt.show()  # Mostrar en pantalla
        print("✅ Gráfico guardado como models/grafico.png")

    except Exception as e:
        print(f"❌ Error durante el entrenamiento del modelo: {e}")


