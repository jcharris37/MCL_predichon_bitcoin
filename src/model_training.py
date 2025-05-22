import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
import matplotlib.pyplot as plt
import pickle

def train_model(data):
    # Verificar que las columnas necesarias existen
    required_cols = ['Open', 'High', 'Low', 'Volume', 'MA_7', 'Close']
    missing_cols = [col for col in required_cols if col not in data.columns]
    if missing_cols:
        raise KeyError(f"❌ Faltan columnas requeridas: {missing_cols}")

    # Preparar las características y la variable objetivo
    X = data[['Open', 'High', 'Low', 'Volume', 'MA_7']]
    y = data['Close']
    
    # Verificar si hay valores NaN en X o y
    if X.isnull().values.any() or y.isnull().values.any():
        print("Hay valores NaN en los datos. Eliminando filas con NaN.")
        data = data.dropna(subset=required_cols)
        if data.empty:
            raise ValueError("❌ No quedan datos después de eliminar filas con NaN.")
        X = data[['Open', 'High', 'Low', 'Volume', 'MA_7']]
        y = data['Close']
    
    # Dividir los datos en entrenamiento y prueba (70% entrenamiento, 30% prueba)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # Crear y entrenar el modelo
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Hacer predicciones y evaluar
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    
    print(f"MSE: {mse}")
    print(f"MAE: {mae}")
    
    return model, y_test, y_pred

if __name__ == '__main__':
    data = pd.read_csv('data/preprocessed_data.csv')
    model, y_test, y_pred = train_model(data)

    # Guardar el modelo entrenado
    with open('models/model.pkl', 'wb') as file:
        pickle.dump(model, file)

    # Graficar resultados
    plt.figure(figsize=(10, 5))
    plt.plot(y_test.values, label='Real', color='blue')
    plt.plot(y_pred, label='Predicho', color='red')
    plt.title("📈 Precio Real vs Predicho (normalizado)")
    plt.xlabel("Índice de muestra")
    plt.ylabel("Precio de cierre (normalizado)")
    plt.legend()
    plt.tight_layout()
    plt.show()


  