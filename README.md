# 💤 Clasificación Binaria – Predicción de Estrés

Este proyecto realiza la **predicción de estrés** basado en hábitos de sueño y parámetros físicos usando modelos de clasificación en Python. Incluye análisis de métricas, comparación de modelos, análisis de errores y una interfaz interactiva con **Gradio**.

---

## 📂 Contenido del proyecto

- `train.csv` – Dataset de entrenamiento.
- `test.csv` – Dataset de prueba.
- `best_model.joblib` – Modelo entrenado.
- `model_columns.pkl` – Columnas del modelo (para codificación de variables categóricas).
- `app.py` – Código principal de la aplicación Gradio.
- `requirements.txt` – Librerías necesarias.

---

## 🔹 Modelos utilizados

Se entrenaron los siguientes modelos:

1. **Random Forest**
2. **Logistic Regression**
3. **Gradient Boosting**
4. **Support Vector Machine (SVM)**

Se calcularon métricas de exactitud, precisión, recall y F1-Score para cada modelo.

---

## 📊 Comparación de métricas

| Modelo                  | Accuracy | Precision | Recall | F1-Score |
|-------------------------|---------|-----------|--------|----------|
| Random Forest           | 0.87    | 0.85      | 0.89   | 0.87     |
| Logistic Regression     | 0.81    | 0.79      | 0.83   | 0.81     |
| Gradient Boosting       | 0.85    | 0.84      | 0.86   | 0.85     |
| Support Vector Machine  | 0.83    | 0.81      | 0.84   | 0.82     |

> Ajusta los valores según los resultados de tus modelos.

---

## 📉 Análisis de errores

### Matriz de confusión – Random Forest
![Random Forest](https://github.com/amymarlene/Modelado-de-datos-Clasificacion-Binaria/blob/main/confusionrandomforest.png?raw=true)

### Matriz de confusión – Logistic Regression
![Logistic Regression](https://github.com/amymarlene/Modelado-de-datos-Clasificacion-Binaria/blob/main/confusionlogisticregression.png?raw=true)

### Matriz de confusión – Gradient Boosting
![Gradient Boosting](https://github.com/amymarlene/Modelado-de-datos-Clasificacion-Binaria/blob/main/confusiongradientboosting.png?raw=true)

### Matriz de confusión – SVM
![SVM](https://github.com/amymarlene/Modelado-de-datos-Clasificacion-Binaria/blob/main/confusionsvm.png?raw=true)

> Las matrices muestran los aciertos y errores de predicción de cada modelo, permitiendo un análisis de errores detallado.

---

## 🚀 Interfaz de usuario

Se incluyó una interfaz interactiva usando **Gradio**, que permite ingresar los datos de una persona y predecir si está en estrés o no.

**Link permanente de la app:**  
[https://huggingface.co/spaces/Amymarlene/stress-prediction](https://huggingface.co/spaces/Amymarlene/stress-prediction)

---

## ⚡ Cómo ejecutar

1. Clona el repositorio:  
```bash
git clone https://github.com/amymarlene/Modelado-de-datos-Clasificacion-Binaria.git
Instala las librerías:

bash
Copiar código
pip install -r requirements.txt
Ejecuta la app de Gradio:

bash
Copiar código
python app.py
Abre el enlace de Hugging Face para usar la app directamente en tu navegador.

📌 Notas
Todos los modelos fueron entrenados usando las columnas:
Gender, Age, Occupation, Sleep Duration, Quality of Sleep, Physical Activity Level, BMI Category, Blood Pressure, Heart Rate, Daily Steps, Sleep Disorder.

El dataset contiene datos de hábitos de sueño y parámetros físicos de cada persona.
