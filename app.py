import os
import json
from flask import Flask, request, jsonify
from openai import OpenAI
from flask_cors import CORS
from dotenv import load_dotenv
from prompt import prompt_text  



# Cargar las variables de entorno
load_dotenv()

# Configurar clave API de OpenAI desde variable de entorno
api_key = os.getenv("OPENAI_API_KEY")

# Crear cliente de OpenAI
client = OpenAI(api_key=api_key)

# Crear la aplicación Flask
app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    try:
        # Obtener el mensaje del usuario desde el cuerpo de la solicitud
        data = request.get_json()
        user_input = data.get('message')
        
        if not user_input:
            return jsonify({'error': 'El campo "message" es obligatorio'}), 400
        
        # Contexto de la conversación
        messages = [
            {"role": "system", "content": prompt_text},
            {"role": "user", "content": user_input}
        ]
        
        # Generar respuesta de OpenAI
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Cambia a "gpt-4" si tienes acceso
            messages=messages,
            max_tokens=4096
        )
        
        # Obtener la respuesta del asistente
        assistant_response = response.choices[0].message.content

        return jsonify({"response": assistant_response})
    
    except Exception as e:
        return jsonify({'error': f'Ocurrió un error: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
