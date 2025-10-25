# 💤 Predicción de Estrés según Hábitos de Sueño

Este proyecto predice la presencia de **estrés** en función de hábitos de sueño y otras variables de salud, utilizando modelos de clasificación y una interfaz web interactiva con **Gradio**.

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
