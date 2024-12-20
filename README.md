# API de Análise de Sentimentos

Este projeto é uma API simples construída com **Flask** e **TextBlob** para analisar o sentimento de um texto (inglês) inserido
pelo usuário. A API responde com a classificação de sentimento (`Positivo`, `Negativo` ou `Neutro`) e o **score** de
polaridade.

## Tecnologias Usadas

- **Python 3.x**
- **Flask** (para a criação da API)
- **TextBlob** (para análise de sentimentos)

## Instalação

1. Clone este repositório:

   ```bash
   git clone https://github.com/NemRela1/sentiment-analysis-api.git
   cd sentiment-analysis-api
   ```

2. Crie e ative um ambiente virtual:
   - **Windows**:
      ```bash
      python -m venv env
      .\env\Scripts\activate
      ```
   - **Mac/Linux**:
      ```bash
      python3 -m venv env
      source env/bin/activate
      ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Execute a API:
   ```bash
   python app.py
   ```
   A API estará disponível em http://127.0.0.1:5000/.

## Usando a API

Para testar a API, envie uma requisição POST para o endpoint /analyze_sentiment com um corpo JSON contendo o texto a ser
analisado.

### Exemplo de requisição com Postman ou cURL:

- **URL**: `http://127.0.0.1:5000/analyze_sentiment`

- **Body** (JSON):
   ```json
   {
     "text": "This is a phrase made with love!"
   }
   ```

### Exemplo de Resposta:

```json
{
    "score": 0.625,
    "sentiment": "Positive"
}
```

### Status de Erro:

```json
{
  "error": "No text provided"
}
```
