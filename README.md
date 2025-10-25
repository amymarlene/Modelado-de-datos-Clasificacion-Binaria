## 🧠 Predicción de Estrés según Hábitos de Sueño

Este proyecto realiza **clasificación binaria** para predecir si una persona presenta estrés o no, basado en sus hábitos de sueño y otros indicadores de salud.  

El proyecto incluye:

- Preprocesamiento de datos (train/test) con manejo de variables categóricas.
- Entrenamiento y comparación de **4 modelos de machine learning**:
  - Random Forest
  - Gradient Boosting
  - Logistic Regression
  - SVM
- Tabla comparativa de métricas: Accuracy, Precision, Recall y F1-Score.
- Análisis de errores con visualización de **matrices de confusión**.
- https://raw.github.com/amymarlene/Modelado-de-datos-Clasificacion-Binaria/blob/main/confusiongradientboosting.png?raw=true
https://raw.github.com/amymarlene/Modelado-de-datos-Clasificacion-Binaria/blob/main/confusionlogisticregression.png?raw=true
https://raw.github.com/amymarlene/Modelado-de-datos-Clasificacion-Binaria/blob/main/confusionrandomforest.png?raw=true
https://raw.github.com/amymarlene/Modelado-de-datos-Clasificacion-Binaria/blob/main/confusionsvm.png?raw=true
- Interfaz de usuario **Gradio** lista para predecir estrés en tiempo real.
- Link permanente a la app desplegada en **Hugging Face Spaces**.

---

## 🔹 Estructura del repositorio

train.csv # Dataset de entrenamiento
test.csv # Dataset de prueba
best_model.joblib # Modelo entrenado guardado
label_encoders.pkl # Encoders para variables categóricas
stress_prediction.ipynb # Notebook con todo el código
requirements.txt # Librerías necesarias
README.md # Este archivo

## 🔹 Instalación y ejecución

1. Clonar el repositorio:

```bash
git clone https://github.com/Amymarlene/stress-prediction.git
cd stress-prediction
Instalar dependencias (recomendado crear un entorno virtual):

bash
Copiar código
pip install -r requirements.txt
Abrir el notebook stress_prediction.ipynb en Google Colab o Jupyter.

Subir train.csv y test.csv al entorno y ejecutar todas las celdas.

Al final del notebook se mostrará un link permanente para abrir la app en Hugging Face:

🌐 Abrir la app permanente en Hugging Face

🔹 Uso de la app
Selecciona los datos de la persona: Edad, Género, Ocupación, Duración de sueño, Calidad de sueño, Actividad física, IMC, Presión arterial, Ritmo cardiaco, Pasos diarios y Trastornos del sueño.

Presiona Predecir Estrés.

La app devolverá:

😌 Sin Estrés

⚠️ Con Estrés


🔹 Métricas y análisis
El notebook genera automáticamente:

Comparación de 4 modelos con Accuracy, Precision, Recall y F1-Score.
<img width="662" height="232" alt="image" src="https://github.com/user-attachments/assets/664d7288-5356-4825-a089-81a0692e2ba6" />


Matrices de confusión para evaluar los errores.

Selección automática del mejor modelo según F1-Score.

🔹 Tecnologías utilizadas
Python 3

Pandas, Numpy

Matplotlib, Seaborn

Scikit-learn

Gradio para UI

Hugging Face Spaces para despliegue

🔹 Contacto
Creado por Amy Frías
GitHub: Amymarlene
Hugging Face: Amymarlene/stress-prediction
