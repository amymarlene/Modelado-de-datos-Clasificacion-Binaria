 # 💤 PREDICCIÓN DE ESTRÉS – GRADIO APP
# Elaborado por: Amy Frías

import pandas as pd
import numpy as np
import joblib
import gradio as gr
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# ======================================================
# 🔹 1. Cargar modelo y columnas
# ======================================================
best_model = joblib.load("best_model.joblib")
model_columns = joblib.load("model_columns.pkl")

# Para el preprocesamiento de categorías
label_encoders = joblib.load("label_encoders.pkl")

# ======================================================
# 🔹 2. Función de predicción
# ======================================================
def predecir_estres(Person_ID, Gender, Age, Occupation, Sleep_Duration, Quality_of_Sleep,
                    Physical_Activity_Level, BMI_Category, Blood_Pressure, Heart_Rate,
                    Daily_Steps, Sleep_Disorder):

    entrada = pd.DataFrame({
        "Gender": [label_encoders["Gender"].transform([Gender])[0]],
        "Age": [Age],
        "Occupation": [label_encoders["Occupation"].transform([Occupation])[0]],
        "Sleep Duration": [Sleep_Duration],
        "Quality of Sleep": [Quality_of_Sleep],
        "Physical Activity Level": [Physical_Activity_Level],
        "BMI Category": [label_encoders["BMI Category"].transform([BMI_Category])[0]],
        "Blood Pressure": [label_encoders["Blood Pressure"].transform([Blood_Pressure])[0]],
        "Heart Rate": [Heart_Rate],
        "Daily Steps": [Daily_Steps],
        "Sleep Disorder": [label_encoders["Sleep Disorder"].transform([Sleep_Disorder])[0]]
    })

    pred = best_model.predict(entrada)[0]
    return "😌 Sin Estrés" if pred == 0 else "⚠️ Con Estrés"

# ======================================================
# 🔹 3. Interfaz Gradio
# ======================================================
with gr.Blocks(theme="soft") as interfaz:
    gr.Markdown("## 🧠 Predicción de Estrés según Hábitos de Sueño")
    gr.Markdown("Ingrese los datos para predecir si existe estrés (0 = No, 1 = Sí)")

    with gr.Row():
        Person_ID = gr.Number(label="Person ID", value=1)
        Gender = gr.Dropdown(list(label_encoders["Gender"].classes_), label="Gender")
        Age = gr.Slider(18, 60, value=25, step=1, label="Age")
        Occupation = gr.Dropdown(list(label_encoders["Occupation"].classes_), label="Occupation")

    with gr.Row():
        Sleep_Duration = gr.Slider(4, 9, value=7, step=0.1, label="Sleep Duration (horas)")
        Quality_of_Sleep = gr.Slider(3, 10, value=7, step=1, label="Quality of Sleep")
        Physical_Activity_Level = gr.Slider(0, 10, value=5, step=1, label="Physical Activity Level")

    with gr.Row():
        BMI_Category = gr.Dropdown(list(label_encoders["BMI Category"].classes_), label="BMI Category")
        Blood_Pressure = gr.Dropdown(list(label_encoders["Blood Pressure"].classes_), label="Blood Pressure")
        Heart_Rate = gr.Number(label="Heart Rate")
        Daily_Steps = gr.Number(label="Daily Steps")
        Sleep_Disorder = gr.Dropdown(list(label_encoders["Sleep Disorder"].classes_), label="Sleep Disorder")

    boton = gr.Button("🔍 Predecir Estrés")
    salida = gr.Textbox(label="Resultado")
    boton.click(fn=predecir_estres,
                inputs=[Person_ID, Gender, Age, Occupation, Sleep_Duration, Quality_of_Sleep,
                        Physical_Activity_Level, BMI_Category, Blood_Pressure, Heart_Rate,
                        Daily_Steps, Sleep_Disorder],
                outputs=salida)

interfaz.launch()
