import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def preprocess_data(data):
    # Asegurar que las columnas sean strings simples
    data.columns = [col[0].capitalize() if isinstance(col, tuple) else col.capitalize() for col in data.columns]


    # ✅ Definir las columnas numéricas esperadas
    numeric_columns = ['Open', 'High', 'Low', 'Close', 'Volume']

    # ✅ Verificar que las columnas existen
    missing_cols = [col for col in numeric_columns if col not in data.columns]
    if missing_cols:
        raise KeyError(f"❌ Faltan columnas numéricas requeridas: {missing_cols}")

    # ✅ Convertir a valores numéricos
    data[numeric_columns] = data[numeric_columns].apply(pd.to_numeric, errors='coerce')

    # ✅ Eliminar filas con valores faltantes
    data.dropna(inplace=True)

    # ✅ Verificar que hay suficientes datos para calcular MA_7
    if len(data) < 7:
        print("❌ No hay suficientes datos para calcular MA_7")
        return pd.DataFrame()  # Retorna DataFrame vacío

    # ✅ Calcular la media móvil de 7 días
    data['MA_7'] = data['Close'].rolling(window=7).mean()

    # ✅ Eliminar NaN generados por el promedio móvil
    data.dropna(inplace=True)

    # ✅ Normalizar los datos
    cols_to_scale = ['Open', 'High', 'Low', 'Close', 'Volume', 'MA_7']
    scaler = MinMaxScaler()
    data[cols_to_scale] = scaler.fit_transform(data[cols_to_scale])

    return data

# 👇 Solo se ejecuta si corres este archivo directamente
if __name__ == '__main__':
    data = pd.read_csv('data/bitcoin_data.csv')
    data = preprocess_data(data)
    data.to_csv('data/preprocessed_data.csv', index=False)
    print("✅ Preprocesamiento completado y guardado en data/preprocessed_data.csv")
