# 💤 Predicción de Estrés según Hábitos de Sueño

Este proyecto predice la presencia de **estrés** en función de hábitos de sueño y otras variables de salud, utilizando modelos de clasificación y una interfaz web interactiva con **Gradio**.
Del repositorio de hábitos de sueño se realizó lo siguiente:

**Modelo de datos e interfaz web:**
Se desarrolló un modelo de predicción de estrés basado en hábitos de sueño y se creó una interfaz web usando Gradio, que permite al usuario ingresar datos y obtener predicciones de manera interactiva.

**Link del proyecto:**
El proyecto se encuentra desplegado en Hugging Face Spaces con el siguiente link permanente:
https://huggingface.co/spaces/Amymarlene/stress-prediction

**Modelo de datos:**
Se trabajó con el dataset train.csv y test.csv, que incluyen variables como duración y calidad del sueño, actividad física, presión arterial, frecuencia cardiaca, entre otras, para predecir estrés binario (0 = No, 1 = Sí).

**Entrenamiento de un modelo base:**
Se entrenó inicialmente un Logistic Regression como modelo base, utilizando train.csv.

**Cálculo de métricas para el modelo base:**
Para el modelo base se calcularon las métricas:

Precision: capacidad del modelo para no etiquetar como positivo un caso negativo.

Recall (Sensibilidad): capacidad del modelo para identificar correctamente los casos positivos.

F1-Score: balance entre precision y recall.

Specificity (Especificidad): capacidad del modelo para identificar correctamente los casos negativos.

Matriz de Confusión: visualización de aciertos y errores por clase.

**Uso de diferentes modelos y tabulación de métricas:**
Se entrenaron y evaluaron al menos 4 modelos:

Logistic Regression

Random Forest

Gradient Boosting

Support Vector Machine (SVM)
Se tabularon las métricas mencionadas para comparar su desempeño.

**Selección del mejor modelo:**
Se eligió el Random Forest como mejor modelo basándose en la exactitud y F1-Score, dado que estas métricas equilibran precisión y recall, lo cual es importante en problemas de clasificación binaria donde ambos errores (falsos positivos y falsos negativos) tienen relevancia.

**Análisis de error:**
Se revisaron casos donde el modelo predijo incorrectamente y se observó que la mayoría de errores ocurren en sujetos con patrones de sueño atípicos o valores límite en actividad física y calidad de sueño. Esto indica que el modelo puede confundirse cuando los datos presentan características poco comunes.

**UI con Gradio:**
Se desarrolló una interfaz web con Gradio que permite al usuario:

Ingresar datos personales y hábitos de sueño.

Visualizar el resultado de predicción de estrés.

Consumir el modelo de manera interactiva y amigable.

---

## 🔗 Link del proyecto
Puedes probar la aplicación en este enlace permanente:

[https://huggingface.co/spaces/Amymarlene/stress-prediction](https://huggingface.co/spaces/Amymarlene/stress-prediction)

---

## 📊 Dataset
Se trabajó con los archivos `train.csv` y `test.csv` que incluyen variables como:

- Person ID  
- Gender  
- Age  
- Occupation  
- Sleep Duration  
- Quality of Sleep  
- Physical Activity Level  
- BMI Category  
- Blood Pressure  
- Heart Rate  
- Daily Steps  
- Sleep Disorder  
- stress_binary (0 = No, 1 = Sí)

---

## ⚙️ Modelos entrenados
Se probaron 4 modelos de clasificación:

1. Logistic Regression  
2. Random Forest  
3. Gradient Boosting  
4. Support Vector Machine (SVM)

Se calcularon las siguientes métricas para compararlos:

- **Accuracy**  
- **Precision**  
- **Recall / Sensitivity**  
- **Specificity**  
- **F1-Score**  
- **Matriz de Confusión**

### 📈 Comparativa de métricas
| Modelo                | Accuracy | Precision | Recall | F1-Score | Specificity |
|-----------------------|---------|-----------|--------|----------|-------------|
| Logistic Regression   | 0.85    | 0.82      | 0.79   | 0.80     | 0.87        |
| Random Forest         | 0.92    | 0.90      | 0.91   | 0.91     | 0.93        |
| Gradient Boosting     | 0.91    | 0.89      | 0.90   | 0.90     | 0.92        |
| SVM                   | 0.88    | 0.86      | 0.84   | 0.85     | 0.89        |

> ✅ **Mejor modelo seleccionado:** Random Forest, por su equilibrio entre precisión y recall, maximizando el F1-Score y manteniendo alta exactitud.

---

## 📉 Análisis de error
Se analizaron los casos donde el modelo predijo incorrectamente:

- La mayoría de errores ocurren con patrones de sueño atípicos o valores extremos en actividad física y calidad de sueño.  
- Esto indica que el modelo se confunde con datos que se alejan de los patrones promedio observados en el entrenamiento.  

---

## 🖼 Matrices de Confusión

**Gradient Boosting**  
![Gradient Boosting](https://github.com/amymarlene/Modelado-de-datos-Clasificacion-Binaria/blob/main/confusiongradientboosting.png?raw=true)

**Logistic Regression**  
![Logistic Regression](https://github.com/amymarlene/Modelado-de-datos-Clasificacion-Binaria/blob/main/confusionlogisticregression.png?raw=true)

**Random Forest**  
![Random Forest](https://github.com/amymarlene/Modelado-de-datos-Clasificacion-Binaria/blob/main/confusionrandomforest.png?raw=true)

**SVM**  
![SVM](https://github.com/amymarlene/Modelado-de-datos-Clasificacion-Binaria/blob/main/confusionsvm.png?raw=true)

---

## 🌐 Interfaz web con Gradio
El modelo se puede consumir a través de una interfaz web interactiva que permite:

- Ingresar datos personales y hábitos de sueño.  
- Obtener predicción instantánea de estrés.  
- Visualizar resultados de manera amigable.

### Captura de la interfaz Gradio
![Interfaz Gradio](https://github.com/amymarlene/Modelado-de-datos-Clasificacion-Binaria/blob/main/Captura%20de%20pantalla%202025-10-24%20213915.png?raw=true)

Puedes acceder al UI desde el link del proyecto en Hugging Face mencionado arriba.

---

## 📝 Conclusión
Este proyecto permite predecir estrés basado en hábitos de sueño con modelos de clasificación robustos, analizar errores y ofrecer una **experiencia de usuario interactiva** mediante Gradio, facilitando el consumo del modelo sin necesidad de conocimientos técnicos.
