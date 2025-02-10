import ollama

resposta = ollama.chat(model='mistral', messages=[{'role': 'user', 'content': 'Explique a teoria da relatividade'}])
print(resposta['message']['content'])
