# FIAP Tech Challenge — Fase 1

Projeto acadêmico de classificação de casos benignos e malignos com regressão logística e árvore de decisão. O primeiro notebook explora a tabela e propõe um exercício de separação das entradas e do alvo.

## Ambiente no Windows

Na pasta do projeto, usando Python 3.14.10 e PowerShell. Se a pasta `.venv` já estiver preparada, abra o notebook diretamente.

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pip check
.\.venv\Scripts\python.exe main.py
```

O `requirements.txt` fixa as versões das bibliotecas listadas no guia. O instalador resolve as demais dependências para o sistema em uso.

O `main.py` verifica se as bibliotecas estão disponíveis. Abra esta pasta no VS Code e selecione `.venv\Scripts\python.exe` como kernel de `notebooks/01_exploracao.ipynb`. Para usar o JupyterLab:

```powershell
.\.venv\Scripts\python.exe -m jupyter lab
```

## Dados

Baixe o arquivo `data.csv` da [base Breast Cancer Wisconsin (Diagnostic)](https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data/data) e salve em `data/raw/data.csv`. A base e o ambiente virtual ficam fora do Git.

## Docker

Para construir a imagem e verificar as dependências:

```powershell
docker build -t fiap-fase1 .
docker run --rm fiap-fase1
```
