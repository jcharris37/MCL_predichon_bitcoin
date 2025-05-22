


# 📈 Predicción de Precio de Bitcoin con Flask y Machine Learning

Este proyecto permite predecir el precio de cierre del Bitcoin utilizando aprendizaje automático. Incluye una API Flask, procesamiento de datos, visualización de resultados y pruebas.

## 🚀 Características

- Descarga automática de datos históricos de Bitcoin desde Yahoo Finance (`yfinance`)
- Preprocesamiento de datos con normalización y cálculo de media móvil
- Entrenamiento de modelo de regresión
- API REST en Flask para realizar predicciones
- Visualización de resultados (precio real vs. predicho)

## 🧠 Estructura del Proyecto

```
/project-root
│
├── data/
│   ├── bitcoin_data.csv        # Datos originales descargados
│   └── preprocessed_data.csv   # Datos limpios y normalizados
│
├── models/
│   ├── model.pkl               # Modelo entrenado
│   └── grafico.png             # Gráfico real vs predicho
│
├── scripts/
│   ├── data_fetching.py        # Script para descargar datos históricos yfinance
│   ├── preprocess.py           # Script para limpiar y preparar datos
│   ├── model_training.py       # Lo entrena y lo guarda en model.pkl
│   └── run_pipeline.py         # Ejecuta todo el pipeline de forma ordenada
│
├── app.py                      # API + Flask
└── README.md                   # Documentación
```


### ⚙️ Requisitos
Instala las dependencias necesarias:
pip install -r requirements.txt

## 🛠 Instrucciones

### Paso 1️⃣: Ejecutar

```bash
python run_pipeline.py
```

Este script se encarga de:

- Descargar los datos (`data_fetching.py`)
- Preprocesarlos (`data_preprocessing.py`)
- Entrenar el modelo (`model_training.py`)
- Guardar gráfico de validación (`grafico.png`)

---

### Paso 2️⃣: Ejecutar

```bash
python app.py
```

Esto iniciará el servidor de la API Flask.

---

### Paso 3️⃣: Probar la API

Como aún no tenemos una interfaz visual, podemos probar la API con:

```bash
python probar_api.py
```

Este script realiza una petición `POST` al endpoint `/predict` con un JSON de prueba como el siguiente:

```json
{
  "Open": 0.45,
  "High": 0.48,
  "Low": 0.43,
  "Volume": 0.60,
  "MA_7": 0.52
}
```


### 🧠 Informacion Adicional
- Se usa yfinance para obtener datos de BTC desde 2020.
- Se normalizan las variables con MinMaxScaler.
- Se calcula la media móvil de 7 días (MA_7).
- El modelo se entrena con regresión lineal simple de sklearn.
- Se utiliza el 70% de los datos para entrenamiento y el 30% restante para validación.

---

### 📊 Resultados
Muestra una grafica con Matplotlib y tambien la guarda en la carpeta models como .png

---

### Creadores:
- [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github&style=flat-square)](https://github.com/jcharris37) Joseph Charris  
- [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github&style=flat-square)](https://github.com/Kevinddg04) Kevin Diaz
- [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github&style=flat-square)](https://github.com/MauroC18) Mauricio Carrillo





          
