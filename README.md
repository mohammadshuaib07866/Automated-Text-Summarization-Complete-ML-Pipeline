# 📘 Automated Text Summarization – Complete ML Pipeline

A **production‑ready end‑to‑end Machine Learning pipeline** for **Abstractive Text Summarization** built using **Hugging Face Transformers, Pegasus model, MLOps principles, and modular architecture**.

This project demonstrates how an industry‑grade NLP system is designed — from **data ingestion to model evaluation** — following clean coding standards and scalable ML engineering practices.

---

## 🚀 Project Overview

Text summarization is a core NLP problem with applications in:

* News summarization
* Chat & conversation summarization
* Document understanding
* Knowledge extraction

In this project, we fine‑tune the **Pegasus model** on the **SAMSum dataset** using a **fully modular, configurable, and reproducible ML pipeline**.

---

## 🧠 Key Features

* ✅ End‑to‑end ML pipeline (Training + Evaluation)
* ✅ Modular folder structure (industry standard)
* ✅ Hugging Face Pegasus model
* ✅ SAMSum dialogue summarization dataset
* ✅ Custom exception & logging system
* ✅ Config‑driven execution (YAML based)
* ✅ MLOps‑ready (easy MLflow / CI‑CD integration)

---

## 🗂️ Project Structure

```
Automated-Text-Summarization-Complete-ML-Pipeline
│
├── main.py
├── params.yaml
├── config/
│   └── config.yaml
│
├── textSummarizer/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   │   └── model_evaluation.py
│   │
│   ├── pipeline/
│   │   └── training_pipeline.py
│   │
│   ├── config/
│   │   └── configuration.py
│   │
│   ├── entity/
│   │   └── entity_config.py
│   │
│   ├── utils/
│   │   └── commons.py
│   │
│   ├── logger/
│   │   └── logging.py
│   │
│   └── exceptions/
│       └── exception.py
│
├── artifacts/
│   ├── data_ingestion/
│   ├── data_transformation/
│   ├── model_trainer/
│   └── model_evaluation/
│
└── README.md
```

---

## ⚙️ Tech Stack

| Category      | Tools                           |
| ------------- | ------------------------------- |
| Language      | Python 3.9+                     |
| Deep Learning | PyTorch                         |
| NLP           | Hugging Face Transformers       |
| Model         | Google Pegasus                  |
| Dataset       | SAMSum                          |
| MLOps         | Modular Pipelines, YAML configs |
| Logging       | Custom Logging Module           |

---

## 📦 Dataset

**SAMSum Dataset**

* Dialogue‑based conversation summaries
* Used for abstractive summarization tasks

Source:

```
https://raw.githubusercontent.com/krishnaik06/datasets/main/summarizer-data.zip
```

---

## 🔧 Configuration Files

### `config/config.yaml`

Controls:

* Dataset URL
* Artifact paths
* Model directories

### `params.yaml`

Controls:

* Model checkpoint
* Tokenizer name
* Training hyperparameters

---

## 🔁 Pipeline Flow

```
main.py
   ↓
TrainingPipeline
   ↓
Data Ingestion
   ↓
Data Transformation (Tokenization)
   ↓
Model Training (Pegasus)
   ↓
Model Evaluation (ROUGE)
```

---

## ▶️ How to Run the Project

### 1️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Run Training Pipeline

```bash
python main.py
```

Artifacts will be created automatically inside the `artifacts/` folder.

---

## 📊 Model Evaluation

* Metric Used: **ROUGE**
* Scores saved as CSV
* Evaluated on test split

Example metrics:

```
rouge1
rouge2
rougeL
rougeLsum
```

---

## 🧪 Error Handling & Logging

* Centralized logging system
* Custom exception class
* Full traceback support
* Production‑safe failure handling

---

## 🧠 ML Engineering Best Practices Used

* Clean architecture
* Config‑driven pipelines
* Separation of concerns
* Reproducibility
* Artifact versioning
* GPU‑aware training

---

## 📌 Future Improvements

* 🔹 MLflow experiment tracking
* 🔹 FastAPI inference service
* 🔹 Docker & AWS deployment
* 🔹 CI/CD pipeline
* 🔹 UI using Streamlit

---

## 👨‍💻 Author

**Mohammad Shuaib**
Certified Data Scientist | ML Engineer | NLP Enthusiast

* Expertise: Data Science, Machine Learning, Deep Learning, MLOps, Generative AI
* Passionate about building scalable ML systems

---

## ⭐ If You Like This Project

Give it a ⭐ on GitHub — it motivates continuous improvement!

---

## 📜 License

This project is licensed for educational and research purposes.

---

> *"Good ML models are trained. Great ML systems are engineered."* 🚀
