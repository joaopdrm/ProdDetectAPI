# ProdDetectAPI

Este projeto é uma API simples para servir um modelo de IA em produção.

## Configuração

### Usando Docker

1. Construa a imagem Docker:
    ```bash
    docker build -t my_project .
    ```

2. Rode o container:
    ```bash
    docker run -p 8000:8000 my_project
    ```

### Usando Docker Compose

1. Construa e inicie os containers:
    ```bash
    docker-compose up --build
    ```

2. A API estará disponível em `http://localhost:8000`.

## Endpoints

### POST /predict
- **Request**: `PredictionRequest`
- **Response**: `PredictionResponse`
