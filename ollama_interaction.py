import requests
import json

# URL do servidor Ollama
url = "http://localhost:11434/api/chat"

# Dados da requisição
payload = {
    "model": "nuextract",  # Certifique-se de que o nome do modelo está correto
    "messages": [{"role": "user", "content": "?"}],
    "stream": False
}

# Cabeçalhos
headers = {"Content-Type": "application/json"}

try:
    # Enviar requisição
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    response.raise_for_status()  # Levanta erro se a resposta não for 200 OK

    # Exibir resposta
    print("Resposta do modelo:", response.json())

except requests.exceptions.RequestException as e:
    print("Erro ao conectar ao servidor:", e)



