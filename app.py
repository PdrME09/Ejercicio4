import openai
from config import Config
import tiktoken

openai.api_base = Config.OPENAI_API_BASE
openai.api_key = Config.OPENAI_API_KEY
openai.api_type = Config.OPENAI_API_TYPE
openai.api_version = Config.OPENAI_API_VERSION

deployment = Config.OPENAI_CHAT_DEPLOYMENT

with open('Correo.txt', 'r', encoding='utf-8') as archivo:
    correo = archivo.read()

conversation = [
    {"role": "system", "content": "You are a email analyzing assistant."},
    {"role": "user", "content": correo}
]

pregunta = """
            Necesito la siguiente información: Nombre de la persona que envía el correo, 
            Nombre de la persona que recibe el correo, Hora del envío, Subject, Listado de Tareas
            Por último necesito que el formato de la respuesta sea un JSON..
            """
conversation.append({"role": "user", "content": pregunta})

response = openai.ChatCompletion.create(
        engine=deployment,
        messages = conversation,
        temperature=0.7,
        max_tokens=150,
        stop=None
    )
print(response['choices'][0]['message']['content'].strip())