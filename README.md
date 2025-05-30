# POC-Cuenta-de-cobro
Se realiza automatización respecto a las cuentas de cobro

# 🧾 Cuenta-de-cobro

`Cuenta-de-cobro` es un proyecto de automatización para la extracción de datos financieros y contables desde archivos PDF de **cuentas de cobro**, utilizando técnicas de OCR y modelos LLM (como Gemini o GPT) para estructurar la información en un formato legible y exportable.

## 📌 Objetivo

Automatizar el procesamiento de archivos PDF con información contable (como nombre del proveedor, valor total, fechas, entre otros) y consolidar los datos extraídos en un archivo `.csv` o `.json`.

## 📂 Estructura del proyecto

```
├── data/ # Carpeta de salida para archivos CSV o JSON generados
├── Cuentas de Cobro Marzo/
├── Cuentas de Cobro Abril/
├── processing
├── prompts
├── config
│
├── main.py # Script principal para ejecutar el pipeline
├── requirements.txt # Dependencias del proyecto
└── README.md # Este archivo
```