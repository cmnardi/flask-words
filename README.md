# Flask-words
Testes de uma API usando Flask 
---
## API de exemplo 
- Testes [PyTest](https://pytest.org)
- Analise estática do código com [PyLint](https://www.pylint.org/)
- Deploy via serverless para AWS Lambda
---
## Subir o ambiente
```
virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt
pytest
python3 main.py
```
---
## Exemplos
Na raiz do projeto foi adicionado um arquivo do [postman](flask_words.postman_collection.json) com exemplos de uso.
É necessário apenas adicionar uma variavel de ambiente _{{host}}_

### Ordenar POST [/order]
Passando uma lista de palavras, é retornada a lista ordenada
Body 
```json 
{"words": ["batman", "robin", "coringa"], "order": "asc"}
```
Response
```json
[
    "batman",
    "coringa",
    "robin"
]
```

### Contar vogais POST [/vowel_count]
Passando uma lista de palavras é retornada cada palavra com sua respectiva quantidade de vogais
Body 
```json 
{"words": ["batman","coringa"]}
```
Response
```json
{
    "batman": 2,
    "coringa": 3
}
```
