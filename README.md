# LensOfLast

**An Intelligent Deep Learning-Based Product Label Recognition, Expiry Monitoring and Inventory Management System**

LensofLast is a solo B.Tech Deep Learning project. It is designed to recognise product-label information from photographs, interpret date fields (MFD, EXP, Best Before, Use By, etc.), validate extracted values, and maintain a digital product inventory.

> This repository is the foundational project scaffold. It includes project structure, setup instructions, dependency manifests, API/UI skeletons, data contracts, experiment plans and documentation. The trained neural networks are intentionally not represented as already completed.

## Project principles

1. **Deep Learning is the core:** the intended research pipeline is image preprocessing → CNN visual features → BiLSTM sequence modelling → attention/decoder experiment → semantic date-field classification.
2. **Never silently guess dates:** uncertain, conflicting or invalid readings must be flagged for user review.
3. **Preserve the package wording:** distinguish EXP, Use By and Best Before. Do not treat all date types as equivalent or claim a product is safe based only on a model prediction.
4. **Separate facts from estimates:** printed dates, calculated dates and user-entered dates must be stored separately.
5. **Build incrementally:** start with a small, reproducible baseline, then add the syllabus experiments.

## Repository map

```text
lensoflast/
├── README.md
├── .gitignore
├── .env.example
├── requirements.txt
├── pyproject.toml
├── package.json
├── docs/
│   ├── PROJECT_BLUEPRINT.md
│   ├── SYLLABUS_MAPPING.md
│   ├── DATASET_SPECIFICATION.md
│   ├── MODEL_PLAN.md
│   ├── EXPERIMENT_PLAN.md
│   ├── API_CONTRACT.md
│   ├── SOLO_ROADMAP.md
│   └── SAFETY_AND_LIMITATIONS.md
├── backend/
│   ├── app/main.py
│   ├── app/api/routes/
│   ├── app/core/
│   ├── app/schemas/
│   ├── app/services/
│   └── tests/
├── frontend/
│   ├── index.html
│   └── src/
├── ml/
│   ├── configs/
│   ├── data/
│   ├── notebooks/
│   ├── src/
│   ├── scripts/
│   ├── tests/
│   └── artifacts/
├── data/
│   ├── raw/
│   ├── interim/
│   ├── processed/
│   ├── annotations/
│   └── external/
└── reports/
    ├── figures/
    └── results/
```

## Prerequisites

- Python **3.11** (recommended for the pinned TensorFlow environment)
- Node.js **20 LTS** and npm
- Git
- A code editor such as VS Code
- Optional: MongoDB local service or MongoDB Atlas connection
- Optional: GPU/CUDA environment. CPU training is supported for small experiments; GPU setup depends on the operating system and hardware.

## Quick start

### 1. Create and activate a Python environment

Windows PowerShell:
```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

macOS/Linux:
```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 2. Configure environment

Copy `.env.example` to `.env` and set values as required. The application can start without MongoDB; database-backed features require a valid `MONGODB_URI`.

### 3. Run the backend

From the repository root:
```bash
uvicorn backend.app.main:app --reload
```
API health endpoint: `http://127.0.0.1:8000/api/v1/health`  
Interactive API docs: `http://127.0.0.1:8000/docs`

### 4. Run the frontend

```bash
npm install
npm run dev
```
Vite prints the local development URL.

### 5. Run tests

```bash
pytest
```

## Development order

1. Finalise label taxonomy and annotation rules.
2. Collect and annotate a small pilot dataset.
3. Build image-quality checks and a reproducible preprocessing pipeline.
4. Establish a non-DL OCR/date-parsing baseline for comparison.
5. Train CNN + sequence-recognition baseline.
6. Add semantic field classification and confidence/review logic.
7. Run controlled syllabus experiments.
8. Connect model inference to the API and UI.
9. Evaluate on a held-out set of unseen product packages.

## Important implementation note

A date parser, regex, barcode lookup or third-party OCR tool may be used as a baseline or supporting utility. They do **not** replace the required trained Deep Learning model. Do not report unimplemented modules as completed, and do not report accuracy until it has been measured on a documented test set.
